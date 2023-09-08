


from path_module import (
                            data_03_04_variant_asset,
                            data_03_01_variant_ldv_entity,
                            data_03_03_geo_entity
                        )
from pxr import Usd, Kind
from os.path import relpath, dirname


ldv_entity_relpath = relpath(data_03_01_variant_ldv_entity, dirname(data_03_04_variant_asset))
geo_entity_relpath = relpath(data_03_03_geo_entity, dirname(data_03_04_variant_asset))

asset_stage = Usd.Stage.CreateNew(data_03_04_variant_asset)
asset_stage.GetRootLayer().subLayerPaths.append(ldv_entity_relpath)
asset_stage.GetRootLayer().subLayerPaths.append(geo_entity_relpath)


asset_root_prim = asset_stage.GetPrimAtPath('/root')
asset_stage.SetDefaultPrim(asset_root_prim)
Usd.ModelAPI(asset_root_prim).SetKind(Kind.Tokens.component)
v_mode = asset_root_prim.GetVariantSet('viewMode')
v_mode.SetVariantSelection('ani')

print(asset_stage.GetRootLayer().ExportToString())
asset_stage.Save()
