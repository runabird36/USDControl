
import functools
from pxr import Usd, UsdGeom, Sdf
from path_module import (
                            data_03_04_variant_asset,
                            data_03_05_magician_setDressing,
                            assetname
                        )
from os.path import relpath, dirname


asset_relpath = relpath(data_03_04_variant_asset, dirname(data_03_05_magician_setDressing))


setDressing_stage = Usd.Stage.CreateNew(data_03_05_magician_setDressing)

len_size = 100
count = 0
interval = 20

assetname = "magicianAcrwd"

for i in range(len_size):
    for j in range(len_size):
        xform_prim = UsdGeom.Xform.Define(setDressing_stage, f"/{assetname}_" + str(count).zfill(3))
        xform_prim.GetPrim().GetReferences().AddReference(asset_relpath)
        
        xform_prim.GetPrim().SetInstanceable(True)
        UsdGeom.XformCommonAPI(xform_prim).SetTranslate((i*interval,0,j*interval))
        count += 1
        
setDressing_stage.SetStartTimeCode(1)
setDressing_stage.SetEndTimeCode(30)


print(setDressing_stage.GetRootLayer().ExportToString())
setDressing_stage.Save()