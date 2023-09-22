# import usd
from importlib import reload
import os
import maya.cmds  as cmds


def get_usd_pythonpath_path() -> str:
    return os.path.join(os.environ["USD_LOCATION"], "lib", "python")

def get_mayapy_path() -> str:
    return "/usr/autodesk/maya2023/bin/mayapy"

def get_usdedit_path() -> str:
    return os.path.join(os.environ["USD_LOCATION"], "bin", "usdcat")




def get_target_path() -> str:
    basicFilter = "*.usd"
    res=cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fileMode=1,okc="import")
    if res == None:
        return
        
    tar_path = res[0]
    return tar_path


def main() -> None:
    pythonpath_tar = get_usd_pythonpath_path()
    mayapy_path = get_mayapy_path()
    
    usdedit_path = get_usdedit_path()
    target_path  = get_target_path()
    
    print("export PYTHONPATH=$PYTHONPATH:{0}".format(pythonpath_tar))
    os.popen("export PYTHONPATH=$PYTHONPATH:{0}".format(pythonpath_tar))
    
    print(mayapy_path + " " + usdedit_path + " " + target_path + " > " + target_path+"a")
    os.popen(mayapy_path + " " + usdedit_path + " " + target_path + " > " + target_path+"a")
    
        
        
main()
    
