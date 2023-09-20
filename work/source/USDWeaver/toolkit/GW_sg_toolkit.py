


import shotgun_api3
import socket


GW_SG = None

def connect_sg():
    global GW_SG
    #===============================================================================
    # Globals
    #===============================================================================
    SERVER_PATH = "https://giantstep.shotgunstudio.com"
    SCRIPT_NAME = 'gweaver_api'
    SCRIPT_KEY = 'xXi9wy_ytmyotwdeykmtkrced'

    #===============================================================================
    # Main
    #===============================================================================
    GW_SG = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY, http_proxy='')
    return GW_SG
    



def query_sg_info() -> dict:

    def query_sg_info_task(GW_SG, hostName) -> dict:
        filters = [['task_assignees.HumanUser.sg_host_name.', 'is', hostName],
                ['project.Project.sg_status', 'is', 'Active'],
                ['sg_status_list', 'not_in', ['fin']],
                ['entity.Shot.code', 'is_not', ''],
                ['entity.Shot.sg_status_list', 'not_in', ['fin', 'omt']],
                ['project.Project.archived', 'is', False]]
        fields = ['project.Project.name',
                'entity.Shot.code'
                ]

        try:
            _res = GW_SG.find('Task', filters, fields)
        except:
            return None

        return _res
    


    global GW_SG
    if GW_SG == None:
        try:
            connect_sg()
        except:
            print("Warnning : shotgrid is not connected !!")
            return None
    hostName = socket.gethostname()
    
    filters = [['sg_host_name', 'is', hostName]]
    fields = ['projects', 'department', 'name', 'login']

    try:
        _MAIN_RES = GW_SG.find_one('HumanUser', filters, fields)
    except:
        return None
    

    # _FILTERED_RES = query_sg_info_task(GW_SG, hostName)

    
    return {"MAIN":_MAIN_RES, "FILTERED":None}
    




# connect_sg()
# aa = query_sg_info()
# from pprint import pprint
# pprint(aa)