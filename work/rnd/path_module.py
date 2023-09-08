
import sys

prj_dir = "/usersetup/pipeline/playground/projects/2023_02_usdPipeline"
data_dir = f"{prj_dir}/data"
code_dir = f"{prj_dir}/work/code"


resource_ldv_00 = f"{data_dir}/00_asset_ldv.usd"


data_00 = f"{data_dir}/00_code_data_01.usd"
data_01 = f"{data_dir}/01_code_data_01.usd"
data_02 = f"{data_dir}/03_code_data_refStage.usd"


# data_06_ldv = f"{data_dir}/ssongBy_ldv.usd"
# data_07_only_ldv = f"{data_dir}/ssongBy_only_ldv.usd"

# data_07_mdl = f"{data_dir}/ssongBy_mdl.usd"
# data_07_asset = f"{data_dir}/ssongBy_asset.usd"


# data_08_setDressing = f"{data_dir}/BigSSongBy_asset.usd"
# data_08_setDressing_small = f"{data_dir}/BigSSongBy_asset_small.usd"
# data_08_setDressing_small10 = f"{data_dir}/BigSSongBy_asset_small10.usd"
# data_08_setDressing_cross = f"{data_dir}/BigSSongBy_asset_cross.usd"



exported_data_magician_mdl          = f"{data_dir}/exportedData/magician_mdl.usd"
exported_data_magician_ldv_render   = f"{data_dir}/exportedData/magician_ldv_render.usd"
exported_data_magician_ldv_ani      = f"{data_dir}/exportedData/magician_ldv_ani.usd"
exported_data_magician_rig          = f"{data_dir}/exportedData/magician_rig.usd"
exported_data_magician_arnold_rig   = f"{data_dir}/exportedData/magician_arnold_rig.usd"



data_02_00_rearranged_ldv       = f"{data_dir}/magician02_rearranged_ldv.usd"
data_02_00_ldv_entity           = f"{data_dir}/magician02_ldv_entity.usd"
data_02_01_rig_entity           = f"{data_dir}/magician02_rig_entity.usd"
data_02_01_magician_asset       = f"{data_dir}/magician02_asset.usd"
data_02_02_magician_setDressing = f"{data_dir}/magician02_groupses.usd"



data_03_00_rearranged_ldv_ani       = f"{data_dir}/magician03/magician03_fragment/magician03_rearraged_ldv_ani.usd"
data_03_00_rearranged_ldv_render    = f"{data_dir}/magician03/magician03_fragment/magician03_rearraged_ldv_render.usd"
data_03_01_variant_ldv_entity       = f"{data_dir}/magician03/magician03_entity/maigician03_variant_ldv_entity.usd"
data_03_02_rearragned_magician_rig  = f"{data_dir}/magician03/magician03_fragment/magician03_rearranged_arnold_rig.usd"
data_03_03_geo_entity               = f"{data_dir}/magician03/magician03_entity/maigician03_variant_geo_entity.usd"
data_03_04_variant_asset            = f"{data_dir}/magician03/magician03_arnold_variant_asset.usd"
data_03_05_magician_reference_setDressing = f"{data_dir}/magician03/magician03_groupses_var_ref.usd"
data_03_05_magician_payload_setDressing   = f"{data_dir}/magician03/magician03_groupses_var_payload.usd"



  



path_list = ['/usersetup/linux/module']

for _path in path_list:
    sys.path.append(_path)



binding_info_render = {'eyeIris_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_pupil_GEO',
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



binding_info_ani = {'magician_belt_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_leather_GEO',
                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_head_GRP/magicianAcrwd_low_head_chainmail_A_steel_GEO'],
 'magician_face_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_gloves_L_leather_GEO',
                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_gloves_R_leather_GEO',
                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_skin_GEO'],
 'magician_inner_cloth_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_surcoat_GRP/magicianAcrwd_low_upperBody_surcoat_B_Fabric_GEO'],
 'magician_robe_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_B_fabric_GEO'],
 'magician_shoes_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_B_steel_GEO',
                       '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_B_steel_GEO',
                       '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_C_steel_GEO',
                       '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_C_steel_GEO'],
 'magician_sign_SG': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_steel_GEO'],
 'magician_staff_01_SG': ['/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_A_wood_GEO'],
 'magician_staff_02_SG': ['/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_C_steel_GEO',
                          '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_A_steel_GEO',
                          '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_B_steel_GEO']}


assetname = "magicianAcrwd"
