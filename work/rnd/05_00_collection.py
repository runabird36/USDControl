# Usd.CollectionAPI.Apply(prim, collection_name)
# collection_api = Usd.CollectionAPI(prim, collection_nam)
# collection_query = collection_api.ComputeMembershipQuery()
### High Level ###
from pxr import Sdf, Usd, UsdUtils
stage = Usd.Stage.CreateInMemory()
bicycle_prim = stage.DefinePrim(Sdf.Path("/set/yard/biycle"), "Cube")
car_prim = stage.DefinePrim(Sdf.Path("/set/garage/car"), "Sphere")
tractor_prim = stage.DefinePrim(Sdf.Path("/set/garage/tractor"), "Cylinder")
helicopter_prim = stage.DefinePrim(Sdf.Path("/set/garage/helicopter"), "Cube")
boat_prim = stage.DefinePrim(Sdf.Path("/set/garage/boat"), "Cube")
set_prim = bicycle_prim.GetParent().GetParent()
set_prim.SetTypeName("Xform")
bicycle_prim.GetParent().SetTypeName("Xform")
car_prim.GetParent().SetTypeName("Xform")
# Create collection
collection_name = "vehicles"
collection_api = Usd.CollectionAPI.Apply(set_prim, collection_name)
collection_api.GetIncludesRel().AddTarget(set_prim.GetPath())
collection_api.GetExcludesRel().AddTarget(bicycle_prim.GetPath())
collection_api.GetExpansionRuleAttr().Set(Usd.Tokens.expandPrims)
print(Usd.CollectionAPI.GetAllCollections(set_prim)) # Returns: [Usd.CollectionAPI(Usd.Prim(</set>), 'vehicles')]
print(Usd.CollectionAPI.GetCollection(set_prim, "vehicles")) # Returns: Usd.CollectionAPI(Usd.Prim(</set>), 'vehicles')
collection_query = collection_api.ComputeMembershipQuery()
print(collection_api.ComputeIncludedPaths(collection_query, stage))
# Returns: [Sdf.Path('/set'), Sdf.Path('/set/garage'), Sdf.Path('/set/garage/car'), Sdf.Path('/set/yard')]
# Set it to explicit only
collection_api.GetExpansionRuleAttr().Set(Usd.Tokens.explicitOnly)
collection_query = collection_api.ComputeMembershipQuery()
print(collection_api.ComputeIncludedPaths(collection_query, stage))
# Returns: [Sdf.Path('/set')]

# To help speed up collection creation, USD also ships with util functions:
# UsdUtils.AuthorCollection(<collectionName>, prim, [<includePathList>], [<excludePathList>])
collection_api = UsdUtils.AuthorCollection("two_wheels", set_prim, [set_prim.GetPath()], [car_prim.GetPath()])
collection_query = collection_api.ComputeMembershipQuery()
print(collection_api.ComputeIncludedPaths(collection_query, stage))
# Returns:
# [Sdf.Path('/set'), Sdf.Path('/set/garage'), Sdf.Path('/set/yard'), Sdf.Path('/set/yard/biycle')]
# UsdUtils.ComputeCollectionIncludesAndExcludes() gives us the possibility to author 
# collections more sparse, that the include to exclude ratio is kept at an optimal size.
# The Python signature differs from the C++ signature:
"""
include_paths, exclude_paths = UsdUtils.ComputeCollectionIncludesAndExcludes(
    target_paths,
    stage,
    minInclusionRatio = 0.75,
    maxNumExcludesBelowInclude = 5,
    minIncludeExcludeCollectionSize = 3,
    pathsToIgnore = [] # This ignores paths from computation (this is not the exclude list)
)		
"""
target_paths = [tractor_prim.GetPath(), car_prim.GetPath(), helicopter_prim.GetPrimPath()]
include_paths, exclude_paths = UsdUtils.ComputeCollectionIncludesAndExcludes(target_paths,stage, minInclusionRatio=.9)
print(include_paths, exclude_paths)
# Returns:
# [Sdf.Path('/set/garage/car'), Sdf.Path('/set/garage/tractor'), Sdf.Path('/set/garage/helicopter')] []
include_paths, exclude_paths = UsdUtils.ComputeCollectionIncludesAndExcludes(target_paths,stage, minInclusionRatio=.1)
print(include_paths, exclude_paths)
# Returns: [Sdf.Path('/set/garage')] [Sdf.Path('/set/garage/boat')]
# Create a collection from the result
collection_api = UsdUtils.AuthorCollection("optimized", set_prim, include_paths, exclude_paths)

print(stage.GetRootLayer().ExportToString())