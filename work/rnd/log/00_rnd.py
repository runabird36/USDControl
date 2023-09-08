


from pxr import Usd
from path_module import data_00, resource_ldv_00

# cur_stage = Usd.Stage.CreateNew(data_00)
# ref_root = cur_stage.OverridePrim("/ryan_root")
# ref_root.GetPayloads().AddPayload(resource_ldv_00)



# cur_stage.GetRootLayer().Save()


ldv_stage = Usd.Stage.Open(resource_ldv_00)

