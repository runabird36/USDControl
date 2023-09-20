# -*- coding:utf-8 -*-

if __name__ == "__main__":
    import os, sys
    main_path = os.path.dirname(os.path.abspath( __file__ ))
    root_dir = os.path.dirname(main_path)
    if root_dir not in sys.path:
        sys.path.append(root_dir)
        
    

from model.data import (GW_user, GW_sg_project, GW_entity, GW_pkg, GW_pub)
from USD_path_module import (get_category_info, get_publishedFiles_info, get_step_element_template,
                            _G_SHOTNAME_CONVENTION_, get_real_path, _G_PKG_DEPARTMENT_LIST_,
                            get_task_from_path, get_format_from_path, get_version_from_path,
                            get_pkg_basic_pipstep_template, DB_TYPE, get_pipestep_list,
                            _G_PKG_DEPARTMENT_LIST_LOWER_)
from general_md_3x import py_toolkit
from re import search, sub, findall
from glob import glob

import os
import re
import time
import logging
import getpass
from pandas import DataFrame
from os import path
from datetime import datetime
from pprint import pprint
from requests import sessions
from rocketchat.api import RocketChatAPI

class HUB():

    __HUB__                 = {}
    __CUR_PRJ__             = ""
    __PRJ_LIST__            = [] 
    __CUR_LINK__            = ""
    __CUR_DEPARTMENT__      = ""
    __CUR_PKG__             = []
    __PUB_LIST__            = []
    __FILTERED_PUBS_LIST__  = []


    def __init__(self) -> None:
        pass


    @property
    def HUB(self) -> dict:
        return self.__HUB__
    @HUB.setter
    def HUB(self, _hub) -> None:
        self.__HUB__ = _hub
    @property
    def CUR_KOR_USER(self) -> str:
        return self.HUB.get("USER").name
    @property
    def CUR_ENG_USER(self) -> str:
        return self.HUB.get("USER").login_name
    @property
    def CUR_PRJ(self) -> str:
        return self.__CUR_PRJ__
    @CUR_PRJ.setter
    def CUR_PRJ(self, _cur_prj) -> None:
        self.__CUR_PRJ__ = _cur_prj
    @property
    def CUR_LINK(self) -> str:
        return self.__CUR_LINK__
    @CUR_LINK.setter
    def CUR_LINK(self, _value :str) -> None:
        self.__CUR_LINK__ = _value
    @property
    def CUR_DEPARTMENT(self) -> None:
        return self.__CUR_DEPARTMENT__
    @CUR_DEPARTMENT.setter
    def CUR_DEPARTMENT(self, _value :str) -> None:
        self.__CUR_DEPARTMENT__ = _value
    @property
    def CUR_PKG(self) -> list:
        return self.__CUR_PKG__
    @CUR_PKG.setter
    def CUR_PKG(self, _value) -> None:
        self.__CUR_PKG__ = _value
    @property
    def CUR_PUBS(self) -> list:
        return self.__PUB_LIST__
    @CUR_PUBS.setter
    def CUR_PUBS(self, _value :list) -> None:
        self.__PUB_LIST__ = _value
    @property
    def CUR_FILTERED_PUBS(self) -> list:
        return self.__FILTERED_PUBS_LIST__
    @CUR_FILTERED_PUBS.setter
    def CUR_FILTERED_PUBS(self, _value :list) -> None:
        self.__FILTERED_PUBS_LIST__ = _value
    
        
    def reformat_raw_data(self, data_type :str, raw_datum) -> None:
        def reformat_user_raw(datum :dict) -> GW_user:
            user_id         = datum.get("id")
            user_name       = datum.get("name")
            user_login      = datum.get("login")
            user_department = datum.get("department").get("name")
            return GW_user.SGuser(
                                    user_id,
                                    user_name,
                                    user_login,
                                    user_department
                                )
        
        def reformat_entity_raw(prj_name :str, datum :dict or DataFrame) -> list:
            sg_entity_list = []
            for idx, cur_row in datum.iterrows():
                if cur_row["entity_type"] == "Shot":
                    link_name   = cur_row['name']
                    if re.fullmatch(_G_SHOTNAME_CONVENTION_, link_name):
                        entity_type = cur_row['type']
                        link_sg_id  = cur_row['id']
                        pipe_steps  = get_pipestep_list(prj_name, link_name)
                        sg_entity_list.append(GW_entity.SGentity("Shot", entity_type, link_name, link_sg_id, pipe_steps))
                elif cur_row["entity_type"] == "Asset":
                    link_name   = cur_row['name']
                    entity_type = cur_row['type'].lower()
                    link_sg_id  = cur_row['id']
                    pipe_steps  = get_pipestep_list(prj_name, entity_type, link_name)
                    sg_entity_list.append(GW_entity.SGentity("Asset", entity_type, link_name, link_sg_id, pipe_steps))
            return sg_entity_list

        def reformat_prj_raw(datum :list) -> list:
            reformated_dict  = {}
            reformated_list  = []
            for _prj_info in datum:
                prj_name    = _prj_info.get("name")
                if not re.search(r"\d{4}\_\d{2}\_\w+", prj_name):
                    continue
                prj_id              = _prj_info.get("id")
                prj_type            = _prj_info.get("type")
                cat_info            = get_category_info(prj_name)
                if isinstance(cat_info, DataFrame):
                    if cat_info.empty == True:
                        continue
                else:
                    if cat_info == None:
                        continue
                # print(cat_info)
                reformated_cat_info = reformat_entity_raw(prj_name, cat_info)
                reformated_dict.update({prj_name : GW_sg_project.SGproject(prj_id, prj_name, prj_type, reformated_cat_info)})
                reformated_list.append(prj_name)
            reformated_list.sort(reverse=True)
            return reformated_dict, reformated_list
        
        if data_type == "USER":
            self.HUB.update({"USER":reformat_user_raw(raw_datum)})
        elif data_type == "PROJECT":
            prj_details, prj_name_list = reformat_prj_raw(raw_datum)
            self.HUB.update({"PROJECT":prj_details, "PROJECT_NAMES":prj_name_list})
        

    def get_prj_list(self) -> list:
        return self.HUB.get("PROJECT_NAMES")

    def get_shots(self, selected_prj :str="") -> dict:
        if selected_prj != "":
            self.CUR_PRJ = selected_prj
        else:
            selected_prj = self.CUR_PRJ
        if self.HUB.get("PROJECT") == None:
            return None
        
        sg_prj_model = self.HUB.get("PROJECT").get(selected_prj)
        category_res = sg_prj_model.category_info
        
        
        # pprint(category_res)
        if category_res == []:
            return None
        return category_res
    


# ================================================================
# Rocket chat part
# ================================================================


    def get_log_file_name(self):
        '''
            example :
            현재 날짜가 2023-03-22 일때 22일은
            0~10, 11~20, 21~31 중에 세번째에 속하므로
            23_03_3.log 파일을 생성하며
            config 모듈에 저장된 로그 경로와 합쳐서 반환
        '''
        current_time = datetime.now()
        c_year = current_time.strftime('%Y')[2:]
        c_mon = current_time.strftime('%m')
        c_day = int(current_time.strftime('%d'))
        if c_day < 11:
            _day = "1"
        elif 10 < c_day < 21:
            _day = "2"
        else:
            _day = "3"
        log_file_name = "Shot_{0}_{1}_{2}.log".format(c_year, c_mon, _day)
        log_file_path = "/usersetup/linux/shotgrid_DB/sg_event_logs/GWeaver/" + log_file_name
        return log_file_path

    def get_logg(self):
        logging.basicConfig(filename=self.get_log_file_name(),
                            format='%(asctime)s %(levelname)s :\n \
                                    \n%(message)s\n' + '-'*70,
                            level=logging.INFO,
                            datefmt='%Y_%m_%d  %I:%M:%S %p')
        return logging

    def conv_check_dataType(self, _list: list, _type: str) -> dict:
        '''
            ['../xxx_characterA_001.abc', '../xxx_characterA_002.abc'] 와 같은 리스트 데이터를
            {'characterA_001.abc' : {'ver': 3, 'path': '../xxx_characterA_001.abc', 'non_ver_path': 'ddd'}, ...}  와 같은 형태로 변환
            외주 데이터로 인해 펍 파일의 경로 및 이름 규약이 다른 파일들이 섞여있는 관계로 가장 고유한 characterA_001.abc 와 같은 이름으로
            데이터를 구분하기 위함
            'non_ver_path' : 한단계 상위 폴더의 이름은 항상 ../v001/.. 과 같은 버전 정보를 담고 있어야 하는데
                             버전 형태의 폴더 이름이 아닐 경우에만 폴더 이름을 추가.
        '''
        _dict = dict()
        for _item in _list:
            if _item.endswith(".abc"):
                if _item.endswith("_cam.abc"):
                    sp_pubFile_name = path.basename(_item)
                    _dict[sp_pubFile_name] = dict()
                    re_ver = re.search(r"[v]([0-9]{3})", _item.split("/")[-2])
                    if not re_ver:
                        if _type == "pre":
                            continue
                        else:
                            _dict[sp_pubFile_name].update({'non_ver_path': _item.split("/")[-2]})
                    _dict[sp_pubFile_name].update({'ver': int(re_ver.group(1)), 'path': _item})
                else:
                    sp_pubFile_name = "_".join(path.basename(_item).split("_")[-2:])
                    _dict[sp_pubFile_name] = dict()
                    re_ver = re.search(r"[v]([0-9]{3})", _item.split("/")[-2])
                    if not re_ver:
                        if _type == "pre":
                            continue
                        else:
                            _dict[sp_pubFile_name].update({'non_ver_path': _item.split("/")[-2]})
                    _dict[sp_pubFile_name].update({'ver': (re_ver.group(1)), 'path': _item})
        return _dict

    def check_data_status(self, _pre: list, _cur: list) -> dict:
        '''
            .../v002/pub_ALA_0010_ani_v002_silian_001.abc
            .../v004/ALA_0010_ani_v004_silian_001.abc
            .../v005/pub_ALA_0010_ani_silian_001.abc
            와 같이 버전별로 통일된 이름 규약을 적용할 수 없는 상태.
            _ 언더바 기준 뒤에서 두번째에서 자른 뒤의 이름을 silian_001 과 같이 고유한 이름을 기준으로 구분하여 데이터 처리.
        '''
        _pre_dict = self.conv_check_dataType(_pre, "pre")
        _cur_dict = self.conv_check_dataType(_cur, "cur")
        _pre_set = set(list(_pre_dict.keys()))
        _cur_set = set(list(_cur_dict.keys()))
        
        removed_set = _pre_set.difference(_cur_set)         # 예전 패키지 버전에 있었다가 사라진 파일 목록
        added_set = _cur_set.difference(_pre_set)           # 새 패키지 버전에 추가된 파일 목록
        intersect_set = _pre_set.intersection(_cur_set)     # 그대로 있는 파일 목록
        
        removed_path_list = [_pre_dict[i]['path'] for i in list(removed_set)]
        added_path_list = [_cur_dict[j]['path'] for j in list(added_set)]
        non_changed_list = list()
        modified_list = list()
        for k in list(intersect_set):
            if _pre_dict[k]['ver'] == _cur_dict[k]['ver']:
                non_changed_list.append(_cur_dict[k]['path'])
            else:
                modified_list.append(_cur_dict[k]['path'])
        _now_timecode = datetime.now().timestamp()
        _now = datetime.fromtimestamp(_now_timecode).strftime('%Y/%m/%d %H:%M')[2:]
        return {'SAVETIME': _now,
                'RMV_PUB': removed_path_list,
                'ADD_PUB': added_path_list,
                'NON_PUB': non_changed_list,
                'MOD_PUB': modified_list}
    
    def get_assigned_users(self, sg, assigned_sg_list: list, _pipe_steps: list, assigned_user_list: list) -> list:
        comp_user_list = list()
        for _assignee in assigned_sg_list:
            if _assignee == None:
                continue
            if _assignee['step'] == None:
                continue
            if not _assignee['step']['name'] in _pipe_steps:
                continue
            if not _assignee['task_assignees']:
                continue
            for _user in _assignee['task_assignees']:
                _name = sg.find_one('HumanUser', [["id", "is", _user['id']], ["sg_status_list", "is", "act"]], ["login"])
                if _name == None:
                    continue
                if _assignee['step']['name'] == "Composite":
                    if not _name['login'] in comp_user_list:
                        print("ADD : " + str(_name['login']))
                        comp_user_list.append(_name['login'])
                else:    
                    if not _name['login'] in assigned_user_list:
                        print("ADD : " + str(_name['login']))
                        assigned_user_list.append(_name['login'])
        return assigned_user_list, comp_user_list

    def get_same_task_assignees(self, sg, project_name, shot_name, pubNotifyDict, shot_step):
        '''
            같은 Shot에 Assign 되어있는 Task - Assignees 목록과
            Linked Asset으로 연결되어있는 Asset - Task - Assignees 목록을 모두 쿼리
        '''
        
        tFilter = [['project.Project.sg_status', 'is', 'Active'],
                   ['project.Project.name', 'is', project_name],
                   ["code", "is", shot_name],
                   ["sg_status_list", "not_in", ["omt", "hld"]]]
        tField = ['id', "code"]
        if shot_step in ["MatchMove", "Animation", "Layout"]:
            tField.append("assets")
        res = sg.find_one("Shot", tFilter, tField)
        
        assigned_user_dict = dict()
        if "assets" in list(res.keys()) and res["assets"]:
            assigned_user_dict["asset"] = list()
            for _asset in res["assets"]:
                tFilter = [["project.Project.name", "is", project_name],
                           ["entity.Asset.code", "is", _asset['name']]]
                tField = ["task_assignees", "content", "sg_status_list", "step"]
                assignedAsset_sg_list = sg.find("Task", tFilter, tField)
                if not assignedAsset_sg_list:
                    continue
                assigned_user_dict["asset"], _res = self.get_assigned_users(sg, assignedAsset_sg_list, pubNotifyDict[shot_step][0], assigned_user_dict["asset"])
        
        tFilter = [["project.Project.name", "is", project_name],
                   ["entity.Shot.code", "is", res["code"]]]
        tField = ["task_assignees", "step"]
        assignedShot_sg_list = sg.find("Task", tFilter, tField)
        if not assignedShot_sg_list and not assigned_user_dict["asset"]:
            return
        assigned_user_dict["shot"] = list()
        assigned_user_dict["shot"], comp_res = self.get_assigned_users(sg, assignedShot_sg_list, pubNotifyDict[shot_step][1], assigned_user_dict["shot"])
        if comp_res:
            assigned_user_dict["comp"] = comp_res
        
        # ADD PM
        res = sg.find_one("Project", [["name", "is", project_name]], ["sg_pm"])
        if not res["sg_pm"]:
            return assigned_user_dict
        
        assigned_user_dict["pm"] = list()
        for _pm in res["sg_pm"]:
            _name = sg.find_one('HumanUser', [["id", "is", _pm['id']], ["sg_status_list", "is", "act"]], ["login"])
            if _name == None:
                continue
            if not _name['login'] in assigned_user_dict["pm"]:
                assigned_user_dict["pm"].append(_name['login'])
        
        return assigned_user_dict

    def checkFX_nukepubfile(self, _file):
        return os.path.splitext(_file)[-1] == ".nk"

    def get_notify_dict(self, project_name: str) -> dict:
        pubNotifyDict = {
                         "FX": ([], ["Lighting"]),
                         "Crowd": ([], ["FX", "Lighting"]),
                         "Lighting": ([], ["FX", "Composite"]),
                         "Shotsculpt": ([], ["Lighting", "FX"]),
                         "Animation": (["Modeling"], ["Lighting", "Shotsculpt", "FX"]),
                         "Layout": (["Modeling"], ["Lighting", "Shotsculpt", "FX", "Animation"])
                         }
        
        if project_name == "2022_06_lostArk":
            pubNotifyDict.update({"CharacterFX": ([], ["Shotsculpt", "Lighting"]),
                                  "Simulation": ([], ["Shotsculpt", "Lighting", "FX"]),
                                  "MatchMove": (['Modeling'], ['Shotsculp', 'Animation', 'Layout', 'Crowd', 'CharacterFX', 'Simulation', 'Lighting', 'FX'])})
        else:
            pubNotifyDict.update({"Hair": ([], ["Shotsculpt", "Lighting"]),
                                  "Cloth": ([], ["Shotsculpt", "Lighting", "FX"]),
                                  "MatchMove": (['Modeling'], ['Shotsculp', 'Animation', 'Layout', 'Crowd', 'Hair', 'Cloth', 'Lighting', 'FX'])})
        
        return pubNotifyDict

    def findUserInGroup(self, user_dict: dict, _user: str) -> dict:
        for notifyGroup in list(user_dict.keys()):
            if _user in user_dict[notifyGroup]:
                return False
        return True

    def add_extra_group(self, user_dict: dict, _whoami: str, department: str) -> dict:
        user_dict["etc"] = ["seokwon.choi"]
        user_dict["me"] = [_whoami]
        if department in ['Shotsculpt', 'Modeling']:
            user_dict["teamLead"] = ['jinchul.kim', 'sunggu.woo']
        elif department in ['FX'] and self.findUserInGroup(user_dict, 'kmglobal'):
            user_dict["teamLead"] = ['kmglobal']
        if "FX" in self.get_notify_dict("Project")[department][1] and self.findUserInGroup(user_dict, 'kmglobal'):
            user_dict["teamLead"] = ['kmglobal']
        
        return user_dict

    def get_rocketchat_api(self):
        session = sessions.Session()
        api = RocketChatAPI(settings={'username': 'bot',
                                      'password': 'Bot@#',
                                      'domain': 'http://10.4.2.21:3000',
                                      'session': session})

        return api

    def get_department_LowCapName_dict(self, sg) -> dict:
        pipeStep_res = sg.find("Step", [], ["code"])
        pipeStep_LowCapName_dict = dict()
        for _step in pipeStep_res:
            pipeStep_LowCapName_dict[_step["code"].lower()] = _step["code"]
        
        return pipeStep_LowCapName_dict

    def get_correct_department_name(self, sg, department: str) -> str:
        pipeStep_LowCapName_dict = self.get_department_LowCapName_dict(sg)
        if department in _G_PKG_DEPARTMENT_LIST_LOWER_:
            department = pipeStep_LowCapName_dict[department]
        return department

    def send_rocketChat_message(self, sg, _model, pubFileList: list, pkg_desc: str):
        logg = self.get_logg()
        logger = logg.getLogger(__name__)
        
        project_name = _model.CUR_PRJ
        shot_name = _model.CUR_LINK
        department = self.get_correct_department_name(sg, _model.CUR_PKG[0])
        pkg_ver = _model.CUR_PKG[1]
        
        pubNotifyDict = self.get_notify_dict(project_name)
        
        if not department in list(pubNotifyDict.keys()):
            return        
        
        '''
            .nk 파일이 패키지에 포함되었을 경우 Composite 팀에 전달되어야 하는 펍 정보일 수 있으므로
            펍 알림 대상에 Composite 팀 추가
        '''
        nkFileList_inText = ""
        if department == "FX":
            nkFileList = list(filter(self.checkFX_nukepubfile, pubFileList))
            if nkFileList:
                pubNotifyDict.update({"FX": ([], ["Composite", "Lighting"])})
                for nkFile in nkFileList:
                    nkFileList_inText += str(nkFile) + "\n"
        
        allPubFileList_inText = ""
        for _pub_item in pubFileList:
            allPubFileList_inText += str(_pub_item) + "\n"
        
        correct_user = {'herirex':'janghyuk.kim', 'kmglobal':'kichun.kim', 'soooh':'soooh.jeong'}
        exception_user = {'janghyuk.kim':'herirex', 'kichun.kim':'kmglobal', 'soooh.jeong':'soooh'}

        user_dict = self.get_same_task_assignees(sg, project_name, shot_name, pubNotifyDict, department)
        
        send_members = ""
        for _grp in list(user_dict.values()):
            for _usr in _grp:
                if _usr in list(exception_user.keys()):
                    send_members += "@" + exception_user[_usr] + ", "
                else:
                    send_members += "@" + _usr + ", "
        
        api = self.get_rocketchat_api()
        
        
        
        _whoami = getpass.getuser()
        # if _whoami in list(correct_user.keys()):
        #     _whoami = correct_user[_whoami]
        user_dict = self.add_extra_group(user_dict, _whoami, department)  # 알림 전달할 예외 그룹 추가
        
        default_info = '_*{0}*_ --- PKG PUB\n{1} - {2}\nPackage Version : {3}\n'.format(project_name, shot_name, department, pkg_ver)
        sendMSG = "@{0} --->  {1}".format(_whoami, send_members[:-2])
        desc_info = "{0}\n\n{1}".format(pkg_desc, sendMSG)

        _user_bs = ""
        for _group in list(user_dict.keys()):
            for _user in user_dict[_group]:
                _user_bs += _user + ", "
                if _user in list(exception_user.keys()):
                    _user = exception_user[_user]
                if _user_bs.count(_user) >= 2:
                    continue
                _chat_room = api.create_im_room(_user, read_only=True)
                
                if _group == "comp":
                    message = '{0}\n{1}\n{2}'.format(default_info, nkFileList_inText, desc_info)
                elif _group == "pm" or _group == "etc":
                    message = '{0}\n{1}\n{2}'.format(default_info, allPubFileList_inText, desc_info)
                else:
                    message = '{0}{1}'.format(default_info, desc_info)
                
                api.send_message(message, _chat_room['id'])
                time.sleep(0.2)
                
        logger.info("{0} -> {1}".format(_whoami, _user_bs))
    
    def clear(self) -> None:
        self.HUB = {}
        self.CUR_PRJ = ""





if __name__ == "__main__":
    
    from general_md_3x import py_toolkit
    from toolkit import GW_sg_toolkit
    
    # sg_thread = py_toolkit.WorkerDict()
    # sg_thread.set_job()
    # sg_thread._job_thread_finished.connect(self.init_hub)
    
    test_prj_name = "2022_09_pipelineEDU2"
    
    query_res = GW_sg_toolkit.query_sg_info()
    
    _model = HUB()
    _model.reformat_raw_data("USER", query_res['MAIN'])
    _model.reformat_raw_data("PROJECT", query_res['MAIN'].get("projects"))
    
    
    prj_list = _model.get_prj_list()
    print(prj_list)
    
    shot_list = _model.get_shots(test_prj_name)
    print(shot_list)