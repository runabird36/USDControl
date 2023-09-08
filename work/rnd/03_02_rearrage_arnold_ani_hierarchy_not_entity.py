

from path_module import (
                            exported_data_magician_arnold_rig,
                            data_03_02_rearragned_magician_rig
                        )
from pxr import Usd, Sdf, UsdGeom


assetname = "magicianAcrwd"

from_stage = Usd.Stage.Open(exported_data_magician_arnold_rig)
from_start_time = from_stage.GetStartTimeCode()
from_end_time   = from_stage.GetEndTimeCode()


to_stage = Usd.Stage.CreateNew(data_03_02_rearragned_magician_rig)
to_grp_prim = UsdGeom.Xform.Define(to_stage, f"/{assetname}_GRP")
to_stage.SetDefaultPrim(to_grp_prim.GetPrim())
to_stage.SetStartTimeCode(from_start_time)
to_stage.SetEndTimeCode(from_end_time)


Sdf.CopySpec(from_stage.GetRootLayer(), f"/{assetname}_rig/geo/{assetname}_GRP", to_stage.GetRootLayer(), f"/{assetname}_GRP")


# print(to_stage.GetRootLayer().ExportToString())
to_stage.Save()




