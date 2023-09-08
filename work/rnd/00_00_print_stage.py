


from path_module import (
                            data_03_04_variant_asset,
                            data_03_01_variant_ldv_entity,
                            data_03_03_geo_entity
                        )
from pxr import Usd

tar_stage = Usd.Stage.Open(data_03_03_geo_entity)
print(tar_stage.GetRootLayer().ExportToString())