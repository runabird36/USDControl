from pxr import Usd, UsdGeom
from path_module import data_01


stage = Usd.Stage.Open(data_01)
xform = stage.GetPrimAtPath('/hello')
sphere = stage.GetPrimAtPath('/hello/world')                # 경로 타고들어가기

print(xform.GetPropertyNames())                             # 각 prim에 있는 Property 리스트 보기
print(sphere.GetPropertyNames())

extent_attr = sphere.GetAttribute('extent')
extent_val = extent_attr.Get()
extent_attr.Set(extent_val*2)


radius_attr = sphere.GetAttribute('radius')
radius_attr.Set(2)




sphere_schema = UsdGeom.Sphere(sphere)                      # Schema 방식으로 가져오기
color = sphere_schema.GetDisplayColorAttr()
color.Set([(0,0,1)])

str_res = stage.GetRootLayer().ExportToString()
print(str_res)


stage.GetRootLayer().Save()