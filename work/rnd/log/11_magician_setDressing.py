
import functools
from pxr import Usd, UsdGeom, Sdf
from path_module import data_09_asset, data_10_magician_setdressing





# setDressing_stage = Usd.Stage.CreateInMemory()
setDressing_stage = Usd.Stage.CreateNew(data_10_magician_setdressing)

tar_asset = Usd.Stage.Open(data_09_asset)

len_size = 10
count = 0
interval = 20

assetname = "magicianAcrwd"

for i in range(len_size):
    for j in range(len_size):
        xform_prim = UsdGeom.Xform.Define(setDressing_stage, f"/{assetname}_" + str(count).zfill(3))
        xform_prim.GetPrim().GetReferences().AddReference(data_09_asset)

        UsdGeom.XformCommonAPI(xform_prim).SetTranslate((i*interval,0,j*interval))
        count += 1
        # print(xform_prim.GetSchemaAttributeNames())

        # add_prim_from_target(setDressing_stage, tar_asset, "/ssongBy_{0}".format(str(i).zfill(3)))


print(setDressing_stage.GetRootLayer().ExportToString())
setDressing_stage.Save()