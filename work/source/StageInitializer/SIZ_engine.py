
import sys, os
from general_md_3x import LUCY, LUCIA

import maya.cmds as cmds
from pxr import Usd, Sdf




def read_and_set(usd_fullpath :str, entity_name, root_prim_name :str) -> None:
    # tar_stage = Usd.Stage.Open(usd_fullpath)
    usd_node = cmds.createNode("mayaUsdProxyShape", n=f"{entity_name}Shape")
    transform_node = cmds.listRelatives(usd_node, p=True)[0]
    cmds.rename(transform_node, entity_name)
    
    cmds.setAttr(f"{usd_node}.filePath", usd_fullpath, type="string")
    
def write_and_set(usd_fullpath :str, entity_name, root_prim_name :str) -> None:
    
    prim_path = Sdf.Path(root_prim_name)
    tar_layer = Sdf.Layer.CreateAnonymous()
    prim_spec = Sdf.CreatePrimInLayer(tar_layer, prim_path)
    prim_spec.nameParent.specifier = Sdf.SpecifierDef
    prim_spec.specifier = Sdf.SpecifierDef

    tar_layer.defaultPrim = "/root"
    
    print(tar_layer.ExportToString())
    tar_layer.Export(usd_fullpath)
    
    
    usd_node = cmds.createNode("mayaUsdProxyShape", n=f"{entity_name}Shape")
    transform_node = cmds.listRelatives(usd_node, p=True)[0]
    cmds.rename(transform_node, entity_name)
    
    cmds.setAttr(f"{usd_node}.filePath", usd_fullpath, type="string")
    


def run() -> None:
    # assets인지 sequence 인지 확인
    
    # usd path 경로 만들기
    # 파일이 있는지 없는지 확인
    # 없으면
        # Sdf.Layer.Export로 write
        # /root/{shot or assetname} 프림 만들기
    # 있으면
        # Usd.Stage.Open 으로 read
    # refresh ?
    
    cur_prj         = LUCY.get_project()
    if cur_prj == None:
        print("Warnning : Is not project path. could not know the projectname", file=sys.stdout)
        return
    
    
    entity_name     = ""
    path_engine     = LUCIA.Path(prj=cur_prj)
    usd_dir         = ""
    usd_fullpath    = ""
    root_prim_name  = ""
    if LUCY.is_assets() == True:
        entity_name         = LUCY.get_assetname()
        usd_dir             = path_engine.get_asset_path()
        root_prim_name      = f"/root/{entity_name}_GRP"
    else:
        entity_name         = LUCY.get_shot()
        usd_dir             = path_engine.get_shot_path()
        root_prim_name      = f"/root/{entity_name}"

    
    usd_fullpath = f"{usd_dir}/{entity_name}.usd"
    
    if os.path.exists(usd_fullpath) == True:
        read_and_set(usd_fullpath, entity_name, root_prim_name)
    else:
        write_and_set(usd_fullpath, entity_name, root_prim_name)
        
        
    
    
    
    
if __name__ == "__main__":
    run()