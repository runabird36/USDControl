
import functools
from pxr import Usd, UsdGeom, Sdf
from path_module import data_07_asset, data_08_setDressing


def add_prim_from_target(stage, target, prim_path=""):
    if not prim_path:
        prim = target.GetDefaultPrim() or target.GetPrimAtPath(
            target.GetRootLayer().defaultPrim
        )
    else:
        prim = target.GetPrimAtPath(prim_path)

    if not prim.IsValid():
        raise RuntimeError(
            'Prim path "{prim_path}" could not be found and there is not '
            "default Prim to fall back on.".format(prim_path=prim_path)
        )

    creators = {
        Sdf.SpecifierClass: stage.CreateClassPrim,
        Sdf.SpecifierDef: functools.partial(
            stage.DefinePrim, typeName=prim.GetTypeName()
        ),
        Sdf.SpecifierOver: stage.OverridePrim,
    }

    creator = creators[prim.GetSpecifier()]
    created_prim = creator(prim.GetPath())

    created_prim.GetReferences().AddReference(
        assetPath=target.GetRootLayer().identifier, primPath=prim.GetPath()
    )




# setDressing_stage = Usd.Stage.CreateInMemory()
setDressing_stage = Usd.Stage.CreateNew(data_08_setDressing)

tar_asset = Usd.Stage.Open(data_07_asset)

len_size = 100
count = 0
interval = 7



for i in range(len_size):
    for j in range(len_size):
        for z in range(len_size):
            
            xform_prim = UsdGeom.Xform.Define(setDressing_stage, "/ssongBy_{0}".format(str(count).zfill(3)))
            xform_prim.GetPrim().GetReferences().AddReference(data_07_asset)

            UsdGeom.XformCommonAPI(xform_prim).SetTranslate((i*interval,j*interval,z*interval))
            count += 1
            # print(xform_prim.GetSchemaAttributeNames())

            # add_prim_from_target(setDressing_stage, tar_asset, "/ssongBy_{0}".format(str(i).zfill(3)))


# print(setDressing_stage.GetRootLayer().ExportToString())
setDressing_stage.Save()