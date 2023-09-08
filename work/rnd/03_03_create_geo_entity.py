


from path_module import (
                            data_03_03_geo_entity, 
                            data_03_02_rearragned_magician_rig
                        )
from pxr import Usd


geo_entity_stage = Usd.Stage.CreateNew(data_03_03_geo_entity)
root_prim = geo_entity_stage.DefinePrim("/root")
geo_entity_stage.SetDefaultPrim(root_prim)

root_prim.GetReferences().AddReference(data_03_02_rearragned_magician_rig)

geo_entity_stage.Save()

