



import os, sys, re
from glob import glob
from pprint import pprint
main_path = os.path.dirname(os.path.abspath( __file__ ))
if "\\" in main_path:
    main_path = main_path.replace("\\", "/")

path_list = [
                main_path,
                "/usersetup/linux/module"
            ]

for _path in path_list:
    if _path not in sys.path:
        sys.path.append(_path)

from general_md_3x import py_toolkit


"""
# Methods to centralize the OS tests and provide a standard way of determining
# the current OS.
"""

import sys, os, tempfile, json
# ========================================================================================
#                           Variable
# ========================================================================================
_G_SHOTNAME_CONVENTION_ = r"[a-zA-Z]{3}\_\d{4}"

_G_SHOT_DEPARTMENT_LIST_ = ["VisualConcept", "MatchMove", "Layout", "Animation",
                            "Shotsculpt", "Crowd", "Simulation", "Lighting", "FX",
                            "Cloth"]
_G_SHOT_DEPARTMENT_LIST_LOWER_ = ["visualconcept", "matchmove", "layout", "animation",
                                "shotsculpt", "crowd", "simulation", "lighting", "fx",
                                "cloth"]

_G_ASSET_DEPARTMENT_LIST_ = ["VisualConcept", "Modeling", "LookDev", "Rigging",
                            "Hair", "Cloth", "Animation",  "FX"]
_G_ASSET_DEPARTMENT_LIST_LOWER_ = ["visualconcept", "modeling", "lookdev", "rigging",
                            "hair", "cloth", "animation",  "fx"]

_G_DEPARTMENT_LIST_        = _G_SHOT_DEPARTMENT_LIST_ + _G_ASSET_DEPARTMENT_LIST_
_G_DEPARTMENT_LIST_LOWER_   = _G_SHOT_DEPARTMENT_LIST_LOWER_ + _G_ASSET_DEPARTMENT_LIST_LOWER_


_icons_dirpath          = main_path + "/" + "icons"
file_icon_dict = {}
file_icon_dict['.abc'] = {'format': 'alembic cache', 'icon': _icons_dirpath + '/alembic_black_icon_6_34.png'}
file_icon_dict['.mov'] = {'format': 'quick time video', 'icon':  _icons_dirpath + '/mov_icon_7_29.png'}
file_icon_dict['.ma'] = {'format': 'Maya ASCII', 'icon':  _icons_dirpath + '/maya_icon_new_2.png'}
file_icon_dict['.mb'] = {'format': 'Maya Binary', 'icon':  _icons_dirpath + '/maya_icon_new_2.png'}
file_icon_dict['.hichy'] = {'format': 'Mesh hirarchy data', 'icon':  _icons_dirpath + '/hichy_icon_2.png'}
file_icon_dict['.mtlx'] = {'format': 'Material X', 'icon':  _icons_dirpath + '/MaterialX_2_28.png'}
file_icon_dict['.ass'] = {'format': 'ASS', 'icon':  _icons_dirpath + '/ass_icon_resize.png'}
file_icon_dict['.nk'] = {'format': 'NK', 'icon':  _icons_dirpath + '/nuke_icon.png'}
file_icon_dict['.grm'] = {'format': 'GRM', 'icon':  _icons_dirpath + '/pgYeti_icon.png'}
file_icon_dict['.fur'] = {'format': 'FUR', 'icon':  _icons_dirpath + '/pgYeti_icon.png'}
file_icon_dict['.vdb'] = {'format': 'GRM', 'icon':  _icons_dirpath + '/openvdb_icon_transparent.png'}
file_icon_dict['.fbx'] = {'format': 'FBX', 'icon':  _icons_dirpath + '/fbx_icon_resized.png'}
file_icon_dict['.exr'] = {'format': 'EXR', 'icon':  _icons_dirpath + '/exr_icon.png'}
file_icon_dict['.psd'] = {'format': 'PSD', 'icon':  _icons_dirpath + '/psd_icon.png'}
file_icon_dict['.jpg'] = {'format': 'JPG', 'icon':  _icons_dirpath + '/jpg_icon.png'}
file_icon_dict['else'] = {'format': 'FBX', 'icon':  _icons_dirpath + '/tex_img_2_30.png'}

seq_exts    = [".png", ".jpg", ".jpeg", ".cin", ".dpx", ".tiff", ".tif", ".exr", ".psd", ".tga", ".ari", ".gif", ".iff", '.tx', ".ass", ".fur", ".vdb"]

_window_icon = main_path + "/" + "icons" + "/" + "GWeaver_icon.png"

DB_TYPE = "PARQUET"

# ========================================================================================
#                           Function
# ========================================================================================
def is_windows(platform=None):
    """
    Determine if the current platform is Windows.

    :param platform: sys.platform style string, e.g 'linux2', 'win32' or
                     'darwin'.  If not provided, sys.platform will be used.

    :returns: True if the current platform is Windows, otherwise False.
    :rtype: bool
    """
    if platform:
        return platform == "win32"
    return sys.platform == "win32"

def is_linux(platform=None):
    """
    Determine if the current platform is Linux.

    :param platform: sys.platform style string, e.g 'linux2', 'win32' or
                     'darwin'.  If not provided, sys.platform will be used.

    :returns: True if the current platform is Linux, otherwise False.
    :rtype: bool
    """
    if platform:
        return platform.startswith("linux")
    return sys.platform.startswith("linux")

def is_macos(platform=None):
    """
    Determine if the current platform is MacOS.

    :param platform: sys.platform style string, e.g 'linux2', 'win32' or
                     'darwin'.  If not provided, sys.platform will be used.

    :returns: True if the current platform is MacOS, otherwise False.
    :rtype: bool
    """
    if platform:
        return platform == "darwin"
    return sys.platform == "darwin"



def get_open_dir_cmd() -> str:
    if is_linux() == True:
        return "nautilus"
    elif is_windows() == True:
        return "explorer.exe"
    
def get_rv_cmd() -> str:
    if is_linux() == True:
        return "/opt/rv-centos7-x86-64-2022.3.1/bin/rv"



def get_real_path(sg_url_path :str) -> str:
    def is_seq_path(check_tar :str) -> bool:
        if re.search(r"#+(\%23)+", check_tar):
            return True
        else:
            return False
        
    def is_startswith_win_drive(check_tar :str) -> bool:
        if re.search(r"^[a-zA-Z]\:", check_tar):
            return True
        else:
            return False
        
    def get_first_frame_path(check_tar :str) -> str:
        glob_path   = re.sub(r"#+(\%23)+", "*", check_tar)
        glob_res = glob(glob_path)
        if glob_res == []:
            return ""
        return glob_res[0]
    
    if is_windows() == True:
        temp_path = re.sub(r"^file\:\/+", "", sg_url_path)
        if is_startswith_win_drive(temp_path) == True:
            pass
        else:
            temp_path = "X:"+temp_path
        
        if is_seq_path(temp_path) == True:
            temp_path = get_first_frame_path(temp_path)
        return temp_path
            
    elif is_linux() == True:
        temp_path = re.sub(r"^file\:\/+", "", sg_url_path)
        if is_startswith_win_drive(temp_path) == True:
            temp_path = re.sub(r"^[a-zA-Z]\:", "", temp_path)
        else:
            if not re.search(r'^\/[a-zA-Z]+', temp_path):
                temp_path = "/" + temp_path
        if is_seq_path(temp_path) == True:
            temp_path = get_first_frame_path(temp_path)
        return temp_path


def get_icon_path(pub_file_type :str) -> str:
    global file_icon_dict
    # if pub_file_type == "":

    if pub_file_type in file_icon_dict:
        return file_icon_dict.get(pub_file_type).get('icon')
    else:
        return file_icon_dict.get('else').get('icon')







def get_category_path(_prj_name :str) -> str:
    global DB_TYPE
    if DB_TYPE == "JSON":
        if is_windows() == True:
            return 'Z:/linux/scripts/general_sc/loader/prj_json/{0}/category/{0}.json'.format(_prj_name)
        elif is_linux() == True:
            return '/usersetup/linux/scripts/general_sc/loader/prj_json/{0}/category/{0}.json'.format(_prj_name)
    elif DB_TYPE == "PARQUET":
        if is_windows() == True:
            return 'Z:/usersetup/linux/shotgrid_DB/sg_event_DB/{0}/category.parquet'.format(_prj_name)
        elif is_linux() == True:
            return '/usersetup/linux/shotgrid_DB/sg_event_DB/{0}/category.parquet'.format(_prj_name)

def get_category_info(_prj_name :str) -> dict:
    global DB_TYPE
    cat_path = get_category_path(_prj_name)
    if os.path.exists(cat_path) == False:
        return None
    if DB_TYPE == "JSON":
        return py_toolkit.read_json(cat_path)
    elif DB_TYPE == "PARQUET":
        return py_toolkit.parq_to_pandas(cat_path)
        # return (cat_df.values).tolist()
    
def get_publishedFiles_path(_prj_name :str) -> str:
    global DB_TYPE
    if DB_TYPE == "JSON":
        if is_windows() == True:
            return 'Z:/linux/scripts/general_sc/loader/prj_json/{0}/publishFiles/publishes.json'.format(_prj_name)
        elif is_linux() == True:
            return '/usersetup/linux/scripts/general_sc/loader/prj_json/{0}/publishFiles/publishes.json'.format(_prj_name)
    elif DB_TYPE == "PARQUET":
        if is_windows() == True:
            return 'Z:/usersetup/linux/shotgrid_DB/sg_event_DB/{0}/publish.parquet'.format(_prj_name)
        elif is_linux() == True:
            return '/usersetup/linux/shotgrid_DB/sg_event_DB/{0}/publish.parquet'.format(_prj_name)

def get_publishedFiles_info(_prj_name :str) -> dict:
    global DB_TYPE
    publishedFiles_path = get_publishedFiles_path(_prj_name)
    if os.path.exists(publishedFiles_path) == False:
        return None
    if DB_TYPE == "JSON":
        return py_toolkit.read_json(publishedFiles_path)
    elif DB_TYPE == "PARQUET":
        return py_toolkit.parq_to_pandas(publishedFiles_path)

def get_pkg_path(prj_name :str, seq_name :str, shot_name :str) -> str:
    if is_windows() == True:
        return "X:/projects/{PROJECT}/sequence/{SEQUENCE}/{SHOT}/Gpkg.yaml".format(
                                                                                    PROJECT=prj_name,
                                                                                    SEQUENCE=seq_name,
                                                                                    SHOT=shot_name
                                                                                )
    elif is_linux() == True:
        return "/projects/{PROJECT}/sequence/{SEQUENCE}/{SHOT}/Gpkg.yaml".format(
                                                                                    PROJECT=prj_name,
                                                                                    SEQUENCE=seq_name,
                                                                                    SHOT=shot_name
                                                                                )

def get_step_element_template(tar_pipestep :str) -> dict:
    return {
            "DEPARTMENT":tar_pipestep, "PKG_VERSION":
                                        [{
                                            "VERSION_NUM":"v001", 
                                            "PUBS":[],
                                            "DESCRIPTION":""
                                        }]
            }


def get_pkg_basic_template(pipe_step_list :list) -> dict:
    """
    {
        "Master" : [
                        {"DEPARTMENT" : str, "PKG_VERSION" : list
                                                            [{
                                                                "VERSION_NUM" : str,
                                                                "PUBS" : list
                                                            }] 
                                                    }
                    ]
    }
    """
    basic_template = {
                        "Master" : []
                    }
    
    for pipe_step in pipe_step_list:
        if pipe_step == "Master":
            continue
        if pipe_step not in _G_PKG_DEPARTMENT_LIST_LOWER_:
            continue
        basic_template["Master"].append({
                                            "DEPARTMENT":pipe_step, "PKG_VERSION":
                                                                        [{
                                                                            "VERSION_NUM":"v001", 
                                                                            "PUBS":[],
                                                                            "DESCRIPTION":""
                                                                        }]
                                            })
    return basic_template

def get_pkg_basic_pipstep_template(pipe_step :str) -> dict:
    """
    {
        "Master" : [
                        {"DEPARTMENT" : str, "PKG_VERSION" : list
                                                            [{
                                                                "VERSION_NUM" : str,
                                                                "PUBS" : list
                                                            }] 
                                                    }
                    ]
    }
    """
    basic_template = {}
    if pipe_step == "Master":
        return {}
    if pipe_step not in _G_PKG_DEPARTMENT_LIST_LOWER_:
        return {}
    basic_template = {
                                        "DEPARTMENT":pipe_step, "PKG_VERSION":
                                                                    [{
                                                                        "VERSION_NUM":"v001", 
                                                                        "PUBS":[],
                                                                        "DESCRIPTION":""
                                                                    }]
                                        }
    return basic_template


def get_pipestep_list(cur_prj :str, cur_link :str) -> str:
    global _G_PKG_DEPARTMENT_LIST_LOWER_
    cur_seq = cur_link.split('_')[0]
    tar_path = ""
    if is_windows() == True:
        tar_path = "X:/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}".format(
                                                                                            PROJECT_NAME    =cur_prj,
                                                                                            SEQUENCE_NAME   =cur_seq,
                                                                                            SHOT_NAME       =cur_link
                                                                                            )
    elif is_linux() == True:
        tar_path = "/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}".format(
                                                                                            PROJECT_NAME    =cur_prj,
                                                                                            SEQUENCE_NAME   =cur_seq,
                                                                                            SHOT_NAME       =cur_link
                                                                                            )
    if os.path.exists(tar_path) == False:
        return []
    else:
        checked_steps = []
        for dir_name in os.listdir(tar_path):
            if dir_name in _G_PKG_DEPARTMENT_LIST_LOWER_:
                checked_steps.append(dir_name)
        return checked_steps


def get_pipestep_path(cur_prj :str, cur_link :str, cur_pipestep :str) -> str:
    cur_pipestep = cur_pipestep.lower()
    cur_seq = cur_link.split('_')[0]
    tar_path = ""
    if is_windows() == True:
        tar_path = "X:/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}/{PIPESTEP}".format(
                                                                                                    PROJECT_NAME    =cur_prj,
                                                                                                    SEQUENCE_NAME   =cur_seq,
                                                                                                    SHOT_NAME       =cur_link,
                                                                                                    PIPESTEP        =cur_pipestep
                                                                                                    )
    elif is_linux() == True:
        tar_path = "/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}/{PIPESTEP}".format(
                                                                                                    PROJECT_NAME    =cur_prj,
                                                                                                    SEQUENCE_NAME   =cur_seq,
                                                                                                    SHOT_NAME       =cur_link,
                                                                                                    PIPESTEP        =cur_pipestep
                                                                                                    )
    if os.path.exists(tar_path) == False:
        return ""
    else:
        return tar_path

def get_task_path(cur_prj :str, cur_link :str, cur_pipestep :str, cur_task :str) -> str:
    cur_pipestep = cur_pipestep.lower()
    cur_seq = cur_link.split('_')[0]
    tar_path = ""
    if is_windows() == True:
        tar_path = "X:/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}/{PIPESTEP}/{TASK}/pub".format(
                                                                                                    PROJECT_NAME    =cur_prj,
                                                                                                    SEQUENCE_NAME   =cur_seq,
                                                                                                    SHOT_NAME       =cur_link,
                                                                                                    PIPESTEP        =cur_pipestep,
                                                                                                    TASK            =cur_task
                                                                                                    )
    elif is_linux() == True:
        tar_path = "/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}/{PIPESTEP}/{TASK}/pub".format(
                                                                                                    PROJECT_NAME    =cur_prj,
                                                                                                    SEQUENCE_NAME   =cur_seq,
                                                                                                    SHOT_NAME       =cur_link,
                                                                                                    PIPESTEP        =cur_pipestep,
                                                                                                    TASK            =cur_task
                                                                                                    )
    if os.path.exists(tar_path) == False:
        return ""
    else:
        return tar_path
def get_format_path(cur_prj :str, cur_link :str, cur_pipestep :str, cur_task :str, cur_format :str) -> str:
    cur_pipestep = cur_pipestep.lower()
    cur_seq = cur_link.split('_')[0]
    tar_path = ""
    if is_windows() == True:
        tar_path = "X:/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}/{PIPESTEP}/{TASK}/pub/{FORMAT}".format(
                                                                                                    PROJECT_NAME    =cur_prj,
                                                                                                    SEQUENCE_NAME   =cur_seq,
                                                                                                    SHOT_NAME       =cur_link,
                                                                                                    PIPESTEP        =cur_pipestep,
                                                                                                    TASK            =cur_task,
                                                                                                    FORMAT          =cur_format
                                                                                                    )
    elif is_linux() == True:
        tar_path = "/projects/{PROJECT_NAME}/sequence/{SEQUENCE_NAME}/{SHOT_NAME}/{PIPESTEP}/{TASK}/pub/{FORMAT}".format(
                                                                                                    PROJECT_NAME    =cur_prj,
                                                                                                    SEQUENCE_NAME   =cur_seq,
                                                                                                    SHOT_NAME       =cur_link,
                                                                                                    PIPESTEP        =cur_pipestep,
                                                                                                    TASK            =cur_task,
                                                                                                    FORMAT          =cur_format
                                                                                                    )
    if os.path.exists(tar_path) == False:
        return ""
    else:
        return tar_path

def get_task_from_path(full_path :str) -> str:
    TASK_COMPONENT_IDX = 7
    if len(full_path.split('/')) < (TASK_COMPONENT_IDX+1):
        return ""
    if is_windows() == True:
        full_path = full_path.replace("\\", "/")
        return full_path.split('/')[TASK_COMPONENT_IDX]

    elif is_linux() == True:
        return full_path.split('/')[TASK_COMPONENT_IDX]
    

def get_format_from_path(full_path :str) -> str:
    return os.path.splitext(full_path)[-1].replace(".", "")


def get_version_from_path(full_path :str) -> str:
    VERSION_COMPONENT_IDX = 10
    if len(full_path.split('/')) < (VERSION_COMPONENT_IDX+1):
        return ""
    if is_windows() == True:
        full_path = full_path.replace("\\", "/")
        return full_path.split('/')[VERSION_COMPONENT_IDX]

    elif is_linux() == True:
        return full_path.split('/')[VERSION_COMPONENT_IDX]
    

def get_version_from_regular_ex(full_path :str) -> str:
    search_res = re.search(r"\/v[0-9]{3}\/", full_path)
    if search_res:
        return (search_res.group()).replace('/', "")
    else:
        return "경로안에 버전이 없음"
    
if __name__ == "__main__":
    test_prj_name = "2022_09_pipelineEDU2"
    res = get_category_info(test_prj_name)
    pprint(res)