


from path_module import (
                            data_03_04_variant_asset,
                            data_03_01_variant_ldv_entity,
                            data_03_03_geo_entity
                        )
from pxr import Usd



asset_stage = Usd.Stage.CreateNew(data_03_04_variant_asset)
asset_stage.GetRootLayer().subLayerPaths.append(data_03_01_variant_ldv_entity)
asset_stage.GetRootLayer().subLayerPaths.append(data_03_03_geo_entity)


asset_root_prim = asset_stage.GetPrimAtPath('/root')
asset_stage.SetDefaultPrim(asset_root_prim)
v_mode = asset_root_prim.GetVariantSet('viewMode')
v_mode.SetVariantSelection('ani')

print(asset_stage.GetRootLayer().ExportToString())
asset_stage.Save()
