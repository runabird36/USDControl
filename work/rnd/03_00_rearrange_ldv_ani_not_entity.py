from path_module import (exported_data_magician_ldv_ani,
                         data_03_00_rearranged_ldv_ani,
                         binding_info_ani)

from pxr import Usd, Sdf, UsdGeom, UsdShade


assetname = "magicianAcrwd"


to_stage = Usd.Stage.CreateNew(data_03_00_rearranged_ldv_ani)
root_prim = UsdGeom.Xform.Define(to_stage, f'/{assetname}_GRP')
mat_prim  = UsdGeom.Scope.Define(to_stage, f'/{assetname}_GRP/mtl')

to_stage.SetDefaultPrim(root_prim.GetPrim())



from_stage = Usd.Stage.Open(exported_data_magician_ldv_ani)



Sdf.CopySpec(from_stage.GetRootLayer(), f'/{assetname}_GRP/mtl', to_stage.GetRootLayer(), f'/{assetname}_GRP/mtl')


for _mat, _geo_list in binding_info_ani.items():
    mat_prim = to_stage.GetPrimAtPath(f"/{assetname}_GRP/mtl/{_mat}")
    for _geo in _geo_list:
        geo_prim = to_stage.OverridePrim(f"{_geo}")
        print(geo_prim, "-->", mat_prim)
        UsdShade.MaterialBindingAPI(geo_prim).Bind(UsdShade.Material(mat_prim))



print(to_stage.GetRootLayer().ExportToString())
to_stage.Save()


