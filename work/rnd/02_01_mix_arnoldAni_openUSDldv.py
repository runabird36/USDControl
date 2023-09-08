

from path_module import (
                            data_02_00_rearranged_ldv,
                            exported_data_magician_arnold_rig,
                            data_02_01_rig_entity,
                            data_02_00_ldv_entity,
                            data_02_01_magician_asset,
                            binding_info_render,
                            assetname)


from pxr import Usd, UsdShade


rig_stage = Usd.Stage.Open(exported_data_magician_arnold_rig)
rig_stage.SetDefaultPrim(rig_stage.GetPrimAtPath(f"/{assetname}_rig"))
rig_stage.Save()

rig_entity_stage = Usd.Stage.CreateNew(data_02_01_rig_entity)
root_prim = rig_entity_stage.DefinePrim("/root")
root_prim.GetReferences().AddReference(data_02_00_ldv_entity)
rig_entity_stage.SetDefaultPrim(root_prim)
rig_entity_stage.Save()




arnold_ani_stage = Usd.Stage.CreateNew(data_02_01_magician_asset)
arnold_ani_stage.GetRootLayer().subLayerPaths.append(data_02_01_rig_entity)
arnold_ani_stage.GetRootLayer().subLayerPaths.append(data_02_00_rearranged_ldv)


root_prim = arnold_ani_stage.DefinePrim("/root")
arnold_ani_stage.SetDefaultPrim(root_prim)
print(arnold_ani_stage.GetRootLayer().ExportToString())

for _mat, _geo_list in binding_info_render.items():
    mat_prim = arnold_ani_stage.GetPrimAtPath(f"/root/mtl/{_mat}")
    for _geo in _geo_list:
        geo_prim = arnold_ani_stage.OverridePrim(f"/root/geo"+_geo)
        print(geo_prim, "-->", mat_prim)
        UsdShade.MaterialBindingAPI(geo_prim).Bind(UsdShade.Material(mat_prim))

arnold_ani_stage.Save()
