


from path_module import (data_09_only_ldv_magician, data_09_ldv_magician,
                        data_09_asset, data_09_mdl_magician, data_13_magician_ani,
                        data_14_magician_asset)

from pxr import Usd, UsdShade


# asset_info = giantUSD.get_assigned_info()
asset_info = {'eyeIris_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_pupil_GEO',
                '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_L_eye_GRP/magicianAcrwd_low_body_L_eye_pupil_GEO',
                '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_iris_GEO',
                '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_L_eye_GRP/magicianAcrwd_low_body_L_eye_iris_GEO'],
 'magicStaff_A_wood_SG': ['/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_A_wood_GEO'],
 'magicStaff_steel_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_Bc_steel_GEO',
                         '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_B_steel_GEO',
                         '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_C_steel_GEO',
                         '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_A_steel_GEO'],
 'magicianA_blood_BeltLeather_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_steel_GEO',
                                    '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_leather_GEO'],
 'magicianA_blood_Chainmail_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_head_GRP/magicianAcrwd_low_head_chainmail_A_steel_GEO'],
 'magicianA_blood_Fabric_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_head_GRP/magicianAcrwd_low_head_hood_A_fabric_GEO',
                               '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_pants_leather_GEO',
                               '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_surcoat_GRP/magicianAcrwd_low_upperBody_surcoat_A_Fabric_GEO',
                               '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_A_fabric_GEO',
                               '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_surcoat_GRP/magicianAcrwd_low_upperBody_surcoat_B_Fabric_GEO'],
 'magicianA_blood_GloveLeather_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_gloves_L_leather_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_gloves_R_leather_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_leather_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_leather_GEO'],
 'magicianA_blood_Metal_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_A_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_C_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_A_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_Bc_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_C_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_B_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_Bd_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_Bb_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_B_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_Bd_steel_GEO',
                              '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_Bb_steel_GEO'],
 'magicianA_blood_layered_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_skin_GEO'],
 'magicianA_blood_robe_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_B_fabric_GEO'],
 'magicianA_eye_cap_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_cap_GEO',
                          '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_L_eye_GRP/magicianAcrwd_low_body_L_eye_cap_GEO']}
assetname = "magicianAcrwd"

asset_stage = Usd.Stage.CreateNew(data_09_asset)
asset_stage.GetRootLayer().subLayerPaths.append(data_09_only_ldv_magician)
asset_stage.GetRootLayer().subLayerPaths.append(data_09_mdl_magician)

for _mat, _geo_list in asset_info.items():
    mat_prim = asset_stage.GetPrimAtPath(f"/{assetname}_GRP/mtl/{_mat}")
    for _geo in _geo_list:
        asset_stage.OverridePrim(_geo)
        geo_prim = asset_stage.GetPrimAtPath(_geo)

        UsdShade.MaterialBindingAPI(geo_prim).Bind(UsdShade.Material(mat_prim))


asset_stage.SetDefaultPrim(asset_stage.GetPrimAtPath(f"/{assetname}_GRP"))
print(asset_stage.GetRootLayer().ExportToString())
asset_stage.Save()

