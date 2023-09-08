from path_module import data_09_only_ldv_magician, data_09_ldv_magician, data_09_asset, data_09_mdl_magician

from pxr import Usd, Sdf, UsdGeom

# asset_info = giantUSD.get_assigned_info()


assetname = "magicianAcrwd"

geo_path = f'/{assetname}_rig/geo/{assetname}_GRP'
mat_path = f'/{assetname}_rig/geo/{assetname}_GRP/mtl'
to_stage = Usd.Stage.CreateNew(data_09_only_ldv_magician)
root_prim = UsdGeom.Xform.Define(to_stage, geo_path)
mat_prim  = UsdGeom.Scope.Define(to_stage, mat_path)

to_stage.SetDefaultPrim(root_prim.GetPrim())



to_layer = Usd.Stage.Open(data_09_ldv_magician)



Sdf.CopySpec(to_layer.GetRootLayer(), f'/{assetname}_GRP/mtl', to_stage.GetRootLayer(), mat_path)

print(to_stage.GetRootLayer().ExportToString())
to_stage.Save()
