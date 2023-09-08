



# Stage 생성후
# Prim 생성
# ** session layer 개념은 별도


from pxr import Usd, UsdGeom
from path_module import data_01
stage = Usd.Stage.CreateNew(data_01)
xform_prim = UsdGeom.Xform.Define(stage, "/hello")
sphere_prim = UsdGeom.Sphere.Define(stage, "/hello/world")

# stage.GetRootLayer().Save()
print(stage.GetRootLayer().ExportToString())