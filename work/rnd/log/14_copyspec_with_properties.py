from pxr import Usd, Sdf, UsdGeom, UsdSkel
from path_module import data_13_magician_ani, data_14_magician_anicopy



'''
1. GEO 리스트 뽑기
2. 

'''

main_stage = Usd.Stage.Open(data_13_magician_ani)
# str_res = main_stage.GetRootLayer().ExportToString()

# mesh_prim = main_stage.GetPrimAtPath('/magicianAcrwd_rig/geo/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_skin_GEO')
# res = mesh_prim.GetPropertyNames()
# print(res)
# res = mesh_prim.GetAttribute("primvars:skel:jointIndices")







to_stage = Usd.Stage.CreateNew(data_14_magician_anicopy)
xform01 = UsdSkel.Root.Define(to_stage, "/magicianAcrwd_GRP")
xform02 = UsdGeom.Xform.Define(to_stage, "/magicianAcrwd_GRP/jnt")
# xform03 = UsdGeom.Xform.Define(to_stage, "/magicianAcrwd_rig/geo/magicianAcrwd_GRP")
# sphere = UsdGeom.Mesh.Define(to_stage, "/ssongBy_group1/ssongBy_pSphere1")


Sdf.CopySpec(main_stage.GetRootLayer(), '/magicianAcrwd_rig.extent', to_stage.GetRootLayer(), "/magicianAcrwd_GRP.extent")
# Sdf.CopySpec(main_stage.GetRootLayer(), '/magicianAcrwd_rig.extent.timeSamples', to_stage.GetRootLayer(), "/magicianAcrwd_GRP.extent.timeSamples")
Sdf.CopySpec(main_stage.GetRootLayer(), '/magicianAcrwd_rig/geo/magicianAcrwd_GRP', to_stage.GetRootLayer(), "/magicianAcrwd_GRP")
Sdf.CopySpec(main_stage.GetRootLayer(), '/magicianAcrwd_rig/rig/jnt', to_stage.GetRootLayer(), "/magicianAcrwd_GRP/jnt")


check_tar = "/magicianAcrwd_GRP/magicianAcrwd_char_GRP/magicianAcrwd_low_GRP/magicianAcrwd_low_body_GRP/magicianAcrwd_low_body_skin_GEO"

check_mesh = to_stage.GetPrimAtPath(check_tar)
print(check_mesh.GetPropertyNames())

for mesh_prim in to_stage.Traverse():
    if UsdGeom.Mesh(mesh_prim):
        binding = UsdSkel.BindingAPI.Apply(mesh_prim)
        binding.CreateSkeletonRel().SetTargets(['/magicianAcrwd_GRP/jnt/Root_M'])


# print(to_stage.GetRootLayer().ExportToString())
to_stage.Save()
