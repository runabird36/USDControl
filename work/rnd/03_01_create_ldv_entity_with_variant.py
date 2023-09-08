





from path_module import (
                            data_03_01_variant_ldv_entity,
                            data_03_00_rearranged_ldv_ani,
                            data_03_00_rearranged_ldv_render
                        )


from pxr import Usd


ldv_entity_stage = Usd.Stage.CreateNew(data_03_01_variant_ldv_entity)
root_prim = ldv_entity_stage.DefinePrim("/root")
ldv_entity_stage.SetDefaultPrim(root_prim)

v_mode = root_prim.GetVariantSets().AddVariantSet("viewMode")
v_mode.AddVariant("ani")
v_mode.AddVariant("render")

v_mode.SetVariantSelection('ani')
with v_mode.GetVariantEditContext():
    root_prim.GetReferences().AddReference(data_03_00_rearranged_ldv_ani)

v_mode.SetVariantSelection('render')
with v_mode.GetVariantEditContext():
    root_prim.GetReferences().AddReference(data_03_00_rearranged_ldv_render)



print(ldv_entity_stage.GetRootLayer().ExportToString())
ldv_entity_stage.Save()

