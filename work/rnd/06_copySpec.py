


from path_module import data_07_mdl, data_06_ldv, data_07_only_ldv



from pxr import Usd, Sdf, UsdGeom


to_stage = Usd.Stage.CreateNew(data_07_only_ldv)
root_prim = UsdGeom.Xform.Define(to_stage, '/ssongBy_group1')
mat_prim  = UsdGeom.Scope.Define(to_stage, '/ssongBy_group1/mtl')

to_stage.SetDefaultPrim(root_prim.GetPrim())



to_layer = Usd.Stage.Open(data_06_ldv)



Sdf.CopySpec(to_layer.GetRootLayer(), '/ssongBy_group1/mtl', to_stage.GetRootLayer(), '/ssongBy_group1/mtl')

print(to_stage.GetRootLayer().ExportToString())
to_stage.Save()

