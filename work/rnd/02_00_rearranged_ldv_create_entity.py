from path_module import (
                            data_02_00_rearranged_ldv,
                            exported_data_magician_ldv_render,
                            data_02_00_ldv_entity
                        )

from pxr import Usd, Sdf, UsdGeom


assetname = "magicianAcrwd"


to_stage = Usd.Stage.CreateNew(data_02_00_rearranged_ldv)
root_prim = UsdGeom.Xform.Define(to_stage, f'/{assetname}_GRP')
mat_prim  = UsdGeom.Scope.Define(to_stage, f'/{assetname}_GRP/mtl')

to_stage.SetDefaultPrim(root_prim.GetPrim())



to_layer = Usd.Stage.Open(exported_data_magician_ldv_render)



Sdf.CopySpec(to_layer.GetRootLayer(), f'/{assetname}_GRP/mtl', to_stage.GetRootLayer(), f'/{assetname}_GRP/mtl')

print(to_stage.GetRootLayer().ExportToString())
to_stage.Save()




ldv_entity_stage = Usd.Stage.CreateNew(data_02_00_ldv_entity)
root_prim = ldv_entity_stage.DefinePrim("/root")
root_prim.GetReferences().AddReference(data_02_00_rearranged_ldv)
ldv_entity_stage.SetDefaultPrim(root_prim)
ldv_entity_stage.Save()
