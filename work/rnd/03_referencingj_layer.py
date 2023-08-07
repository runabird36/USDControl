


# 기존 asset usda 파일에 
# 1. xform prim 에 defaultPrim 지정 for referencing
# 2. To override, transformation을 root prim에 지정 by xform schema


from pxr import Usd, UsdGeom
from path_module import data_01

stage = Usd.Stage.Open(data_01)
hello_prim = stage.GetPrimAtPath("/hello")
stage.SetDefaultPrim(hello_prim)

UsdGeom.XformCommonAPI(hello_prim).SetTranslate((4,5,6))

stage.GetRootLayer().Save()