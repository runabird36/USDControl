

from pxr import Usd, UsdGeom
from path_module import (
                            data_02_02_magician_setDressing,
                            data_02_01_magician_asset
                        )






setDressing_stage = Usd.Stage.CreateNew(data_02_02_magician_setDressing)


len_size = 20
count = 0
interval = 20

assetname = "magicianAcrwd"

for i in range(len_size):
    for j in range(len_size):
        xform_prim = UsdGeom.Xform.Define(setDressing_stage, f"/{assetname}_" + str(count).zfill(3))
        xform_prim.GetPrim().GetReferences().AddReference(data_02_01_magician_asset)
        
        xform_prim.GetPrim().SetInstanceable(True)

        UsdGeom.XformCommonAPI(xform_prim).SetTranslate((i*interval,0,j*interval))
        count += 1
        
setDressing_stage.SetStartTimeCode(1)
setDressing_stage.SetEndTimeCode(30)


print(setDressing_stage.GetRootLayer().ExportToString())
setDressing_stage.Save()