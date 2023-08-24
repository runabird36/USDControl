
from path_module import data_07_asset, data_07_only_ldv, data_07_mdl
from pxr import Usd, UsdShade

asset_stage = Usd.Stage.CreateNew(data_07_asset)
# asset_stage = Usd.Stage.CreateInMemory()


asset_stage.OverridePrim("/ssongBy_group1")
asset_stage.OverridePrim("/ssongBy_group1/ssongBy_pSphere1")
asset_stage.OverridePrim("/ssongBy_group1/ssongBy_pSphere2")

asset_stage.SetDefaultPrim(asset_stage.GetPrimAtPath("/ssongBy_group1"))

asset_stage.GetRootLayer().subLayerPaths.append(data_07_only_ldv)
asset_stage.GetRootLayer().subLayerPaths.append(data_07_mdl)


prim_of_small = asset_stage.GetPrimAtPath("/ssongBy_group1/ssongBy_pSphere1")
prim_of_large = asset_stage.GetPrimAtPath("/ssongBy_group1/ssongBy_pSphere2")




# only_ldv_stage = Usd.Stage.Open(data_07_only_ldv)
prim_of_mat01 = asset_stage.GetPrimAtPath('/ssongBy_group1/mtl/ssongBy_smallSG')
prim_of_mat02 = asset_stage.GetPrimAtPath('/ssongBy_group1/mtl/ssongBy_largeSG')


UsdShade.MaterialBindingAPI(prim_of_small).Bind(UsdShade.Material(prim_of_mat01))
UsdShade.MaterialBindingAPI(prim_of_large).Bind(UsdShade.Material(prim_of_mat02))


print(asset_stage.GetRootLayer().ExportToString())
asset_stage.Save()


