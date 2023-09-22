# import usd
from importlib import reload
from pxr import Usd
import maya.cmds as cmds



def get_import_path() -> str:
    basicFilter = "*.usd"
    res=cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fileMode=1,okc="import")
    if res == None:
        return
        
    import_path = res[0]
    return import_path


def main() -> None:
    import_path = get_import_path()
    target_stage = Usd.Stage.Open(import_path)
    stage_contents = target_stage.ExportToString()
    print(stage_contents)
        
        
main()
    