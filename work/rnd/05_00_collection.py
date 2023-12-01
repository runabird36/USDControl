

from pxr import Usd, Sdf, UsdUtils, UsdShade
from path_module import (
                            assetname,
                            data_05_00_lambert_magician_setDressing,
                            data_05_00_authorign_collection,
                            binding_info_ani,
                            data_03_00_rearranged_ldv_ani
                        )
from shutil import copyfile


len_size = 5


copyfile(data_05_00_lambert_magician_setDressing, data_05_00_authorign_collection)

root_stage = Usd.Stage.Open(data_05_00_authorign_collection)



asset_grp_prim = root_stage.GetPrimAtPath(Sdf.Path(f"/SET/{assetname}_grp"))
root_prim = root_stage.GetPrimAtPath("/SET")

asset_grp_prim.SetTypeName("xform")
root_prim.SetTypeName("xform")


col_name = f"{assetname}_robe"
col_api = Usd.CollectionAPI.Apply(asset_grp_prim, col_name)


for _idx in range(len_size*len_size):
    
    test_geo_path = binding_info_ani.get("magician_robe_SG")[0]
    
    count = str(_idx).zfill(3)
    xform_path = f"/SET/{assetname}_grp/{assetname}_{count}"
    target_path = test_geo_path.replace(f"/{assetname}_GRP", xform_path)
    add_target_prim = root_stage.GetPrimAtPath(target_path)
    if add_target_prim:
        col_api.GetIncludesRel().AddTarget(Sdf.Path(target_path))
col_api.GetExpansionRuleAttr().Set(Usd.Tokens.expandPrims)
# col_api.ComputeMembershipQuery()

set_prim = root_stage.GetPrimAtPath("/SET")
set_prim.GetReferences().AddReference(data_03_00_rearranged_ldv_ani)

mat_prim = root_stage.GetPrimAtPath("/SET/mtl/magician_robe_SG")

# print(get_bound_material(prim, collection="Erasers").GetPath())
root_prim.ApplyAPI(UsdShade.MaterialBindingAPI)
UsdShade.MaterialBindingAPI(root_prim).Bind(col_api, UsdShade.Material(mat_prim))

root_stage.Save()