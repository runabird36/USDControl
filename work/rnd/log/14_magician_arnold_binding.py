


from path_module import (data_09_only_ldv_magician, data_09_ldv_magician,
                        data_09_asset, data_09_mdl_magician, data_13_magician_ani,
                        data_14_magician_only_ldv, data_14_magician_asset, data_14_magician_ldv)

from pxr import Usd, UsdShade, UsdGeom, Sdf


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

arnold_asset_info = {'eyeIris_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_L_eye_GRP/magicianAcrwd_low_body_L_eye_iris_GEO',
                       '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_pupil_GEO',
                       '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_iris_GEO',
                       '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_L_eye_GRP/magicianAcrwd_low_body_L_eye_pupil_GEO'],
 'magicianACrwdStaffLowMetal_MTL': ['/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_C_steel_GEO',
                                    '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_A_steel_GEO',
                                    '/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_B_steel_GEO',
                                    '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_Bc_steel_GEO'],
 'magicianACrwdStaffLowWood_MTL': ['/magicianAcrwd_GRP/magicianAcrwd_weapon_GRP/magicianAcrwd_low_magicStaff_GRP/magicianAcrwd_low_magicStaff_A_wood_GEO'],
 'magicianA_blood_BeltLeather_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_leather_GEO',
                                           '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_belt_A_GRP/magicianAcrwd_low_lowerBody_belt_Aa_steel_GEO'],
 'magicianA_blood_Chainmail_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_head_GRP/magicianAcrwd_low_head_chainmail_A_steel_GEO'],
 'magicianA_blood_Fabric_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_head_GRP/magicianAcrwd_low_head_hood_A_fabric_GEO',
                                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_surcoat_GRP/magicianAcrwd_low_upperBody_surcoat_A_Fabric_GEO',
                                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_A_fabric_GEO',
                                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_surcoat_GRP/magicianAcrwd_low_upperBody_surcoat_B_Fabric_GEO',
                                      '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_lowerBody_GRP/magicianAcrwd_low_lowerBody_pants_leather_GEO'],
 'magicianA_blood_GloveLeather_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_leather_GEO',
                                            '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_gloves_L_leather_GEO',
                                            '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_gloves_R_leather_GEO',
                                            '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_leather_GEO'],
 'magicianA_blood_Metal_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_Bd_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_R_GRP/magicianAcrwd_low_arm_R_Bb_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_B_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_C_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_C_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_Bb_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_A_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_R_GRP/magicianAcrwd_low_leg_R_B_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_Bd_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_leg_L_GRP/magicianAcrwd_low_leg_L_A_steel_GEO',
                                     '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_arm_L_GRP/magicianAcrwd_low_arm_L_Bc_steel_GEO'],
 'magicianA_blood_layered_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_skin_GEO'],
 'magicianA_blood_robe_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_upperBody_GRP/magicianAcrwd_low_upperBody_B_fabric_GEO'],
 'magicianA_eye_cap_MTL_blood': ['/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_L_eye_GRP/magicianAcrwd_low_body_L_eye_cap_GEO',
                                 '/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_R_eye_GRP/magicianAcrwd_low_body_R_eye_cap_GEO']}
assetname = "magicianAcrwd"



only_ldv_stage = Usd.Stage.CreateNew(data_14_magician_only_ldv)
root_prim = UsdGeom.Xform.Define(only_ldv_stage, f'/{assetname}_GRP')
mat_prim  = UsdGeom.Scope.Define(only_ldv_stage, f'/{assetname}_GRP/look')
only_ldv_stage.SetDefaultPrim(root_prim.GetPrim())


from_ldv_stage = Usd.Stage.Open(data_14_magician_ldv)
for _prim in from_ldv_stage.Traverse():
    if UsdShade.Material(_prim):
        to_mat_prim = UsdShade.Material.Define(only_ldv_stage, Sdf.Path(f'/{assetname}_GRP/look' + _prim.GetPath().pathString))
        Sdf.CopySpec(from_ldv_stage.GetRootLayer(), _prim.GetPath(), only_ldv_stage.GetRootLayer(), to_mat_prim.GetPath())
        
# print(asset_stage.GetRootLayer().ExportToString())
only_ldv_stage.Save()



'''
arnold-maya로 lookdev  export할 시, 
material 이름이 이상하게 들어와있어서 실패

ex) magicianA_blood_layered_MTL_bloodcommanderABody_DisplacementShader
'''
asset_stage = Usd.Stage.CreateNew(data_14_magician_asset)
asset_stage.GetRootLayer().subLayerPaths.append(data_14_magician_only_ldv)
asset_stage.GetRootLayer().subLayerPaths.append(data_09_mdl_magician)

for _mat, _geo_list in arnold_asset_info.items():
    mat_prim = asset_stage.GetPrimAtPath(f"/{assetname}_GRP/look/{_mat}")
    for _geo in _geo_list:
        asset_stage.OverridePrim(_geo)
        geo_prim = asset_stage.GetPrimAtPath(_geo)

        print(f"{geo_prim} --> {mat_prim}")
        # UsdShade.MaterialBindingAPI(geo_prim).Bind(UsdShade.Material(mat_prim))

asset_stage.SetDefaultPrim(asset_stage.GetPrimAtPath(f"/{assetname}_GRP"))
# print(asset_stage.GetRootLayer().ExportToString())
asset_stage.Save()

