
import functools
from pxr import Usd, UsdGeom, Kind
from path_module import (
                            data_03_04_variant_asset,
                            data_03_05_magician_payload_setDressing,
                            data_03_05_magician_100_payload_setDressing,
                            assetname,
                            data_05_00_lambert_magician_setDressing,
                            data_03_02_rearragned_magician_rig
                        )
from os.path import relpath, dirname


asset_relpath = relpath(data_03_02_rearragned_magician_rig, dirname(data_05_00_lambert_magician_setDressing))


setDressing_stage = Usd.Stage.CreateNew(data_05_00_lambert_magician_setDressing)

len_size = 5
count = 0
interval = 20

assetname = "magicianAcrwd"

for i in range(len_size):
    for j in range(len_size):
        xform_prim = UsdGeom.Xform.Define(setDressing_stage, f"/SET/{assetname}_grp/{assetname}_" + str(count).zfill(3))
        xform_prim.GetPrim().GetPayloads().AddPayload(asset_relpath)
        
        # xform_prim.GetPrim().SetInstanceable(True)
        
        
        UsdGeom.XformCommonAPI(xform_prim).SetTranslate((i*interval,0,j*interval))
        count += 1
        
setDressing_stage.SetStartTimeCode(1)
setDressing_stage.SetEndTimeCode(30)


print(setDressing_stage.GetRootLayer().ExportToString())
setDressing_stage.Save()