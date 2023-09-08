





from path_module import (
                            data_03_01_variant_ldv_entity,
                            data_03_00_rearranged_ldv_ani,
                            data_03_00_rearranged_ldv_render
                        )


from pxr import Usd
from os.path import relpath, dirname


ldv_ani_relpath     = relpath(data_03_00_rearranged_ldv_ani, dirname(data_03_01_variant_ldv_entity))
ldv_render_relpath  = relpath(data_03_00_rearranged_ldv_render, dirname(data_03_01_variant_ldv_entity))



ldv_entity_stage = Usd.Stage.CreateNew(data_03_01_variant_ldv_entity)
root_prim = ldv_entity_stage.DefinePrim("/root")
ldv_entity_stage.SetDefaultPrim(root_prim)

v_mode = root_prim.GetVariantSets().AddVariantSet("viewMode")
v_mode.AddVariant("ani")
v_mode.AddVariant("render")

v_mode.SetVariantSelection('ani')
with v_mode.GetVariantEditContext():
    root_prim.GetReferences().AddReference(ldv_ani_relpath)

v_mode.SetVariantSelection('render')
with v_mode.GetVariantEditContext():
    root_prim.GetReferences().AddReference(ldv_render_relpath)



print(ldv_entity_stage.GetRootLayer().ExportToString())
ldv_entity_stage.Save()

