



from pxr import Usd, UsdGeom
from path_module import data_01, data_02


# 기존 asset usda 파일에 
# 1. xform prim 에 defaultPrim 지정 for referencing
# 2. To override, transformation을 root prim에 지정 by xform schema
#
#    *** override 할 항목들이 무엇인지 확인하고, referencing하기전에 schema로 입히기!!!
#
def step_01():
    stage = Usd.Stage.Open(data_01)
    hello_prim = stage.GetPrimAtPath("/hello")
    stage.SetDefaultPrim(hello_prim)

    UsdGeom.XformCommonAPI(hello_prim).SetTranslate((4,5,6))

    stage.GetRootLayer().Save()



# 1. Stage 생성
# 2. override prim 생성
# 3. 레퍼런스 추가
# 4. Xformable schema 추가 --> 변환 (Transformation)을 해당 prim (override) 에서 지정할 수 있도록

def step_02():
    print(data_02)
    ref_stage = Usd.Stage.CreateNew(data_02)                # 1.
    print(type(ref_stage))
    ref_sphere = ref_stage.OverridePrim("/refSphere")       # 2.

    ref_sphere.GetReferences().AddReference(data_01)        # 3.


    ref_xform = UsdGeom.Xformable(ref_sphere)               # 4.
    ref_xform.SetXformOpOrder([])



    ref_stage.GetRootLayer().Save()




def step_03():
    ref_stage = Usd.Stage.Open(data_02)
    
    ref_sphere_02 = ref_stage.OverridePrim('/refSphere02')
    ref_sphere_02.GetReferences().AddReference(data_01)


    ref_stage.GetRootLayer().Save()



# 1. override prim 만 아니라 그 아래, 레퍼런스로 불러온 사람들도 작성 (author) 가능
def step_04():
    ref_stage = Usd.Stage.Open(data_02)

    overed_sphere = UsdGeom.Sphere.Get(ref_stage, "/refSphere02/world")
    overed_sphere.GetDisplayColorAttr().Set([(1,0,0)])

    ref_stage.GetRootLayer().Save()



step_01()

step_02()

step_03()

step_04()