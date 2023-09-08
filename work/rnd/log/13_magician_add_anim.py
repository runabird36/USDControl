


from path_module import data_09_asset, data_13_magician_ani, data_13_magician_arnold_ani, data_13_magician_arnold_anicopy


from pxr import Usd, UsdGeom, Sdf
try:
    assetname = "magicianAcrwd"

    from_ani_stage = Usd.Stage.Open(data_13_magician_arnold_ani)
    to_ani_stage = Usd.Stage.Open(data_13_magician_arnold_anicopy)
    assetname_grp_prim = UsdGeom.Xform.Define(to_ani_stage, f"/{assetname}_GRP")
    to_ani_stage.SetDefaultPrim(assetname_grp_prim.GetPrim())

    Sdf.CopySpec(from_ani_stage.GetRootLayer(), f"/{assetname}_rig/geo/{assetname}_GRP", to_ani_stage.GetRootLayer(), f"/{assetname}_GRP")

    # print(to_ani_stage.GetRootLayer().ExportToString())
    to_ani_stage.Save()




    asset_stage = Usd.Stage.Open(data_09_asset)

    
    if data_13_magician_arnold_anicopy not in asset_stage.GetRootLayer().subLayerPaths:
        asset_stage.GetRootLayer().subLayerPaths.insert(0, data_13_magician_arnold_anicopy)



    print(asset_stage.GetRootLayer().ExportToString())
    asset_stage.Save()
except Exception as e:
    print(str(e))