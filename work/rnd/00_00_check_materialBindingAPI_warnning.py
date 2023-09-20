

from pxr import Usd, UsdShade
from path_module import data_03_04_variant_asset, exported_data_magician_ldv_render
aa = "/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_skin_GEO"
tar_stage = Usd.Stage.Open(exported_data_magician_ldv_render)

tar_prim_str = "/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_steel_GEO"

tar_prim = tar_stage.GetPrimAtPath(aa)
print(tar_prim.HasAPI(UsdShade.MaterialBindingAPI))
