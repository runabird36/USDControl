

from pxr import Sdf

'''
['AncestorsRange', 'AppendChild', 'AppendElementString', 'AppendExpression', 'AppendMapper', 'AppendMapperArg',
'AppendPath', 'AppendProperty', 'AppendRelationalAttribute', 'AppendTarget', 'AppendVariantSelection', 'ContainsPrimVariantSelection',
'ContainsPropertyElements', 'ContainsTargetPath', 'FindLongestPrefix', 'FindLongestStrictPrefix', 'FindPrefixedRange',
'GetAbsoluteRootOrPrimPath', 'GetAllTargetPathsRecursively', 'GetAncestorsRange', 'GetCommonPrefix', 'GetConciseRelativePaths',
'GetParentPath', 'GetPrefixes', 'GetPrimOrPrimVariantSelectionPath', 'GetPrimPath', 'GetVariantSelection', 'HasPrefix',
'IsAbsolutePath', 'IsAbsoluteRootOrPrimPath', 'IsAbsoluteRootPath', 'IsExpressionPath', 'IsMapperArgPath', 'IsMapperPath',
'IsNamespacedPropertyPath', 'IsPrimPath', 'IsPrimPropertyPath', 'IsPrimVariantSelectionPath', 'IsPropertyPath',
'IsRelationalAttributePath', 'IsRootPrimPath', 'IsTargetPath', 'IsValidIdentifier', 'IsValidNamespacedIdentifier',
'IsValidPathString', 'JoinIdentifier', 'MakeAbsolutePath', 'MakeRelativePath', 'RemoveAncestorPaths', 'RemoveCommonSuffix',
'RemoveDescendentPaths', 'ReplaceName', 'ReplacePrefix', 'ReplaceTargetPath', 'StripAllVariantSelections', 'StripNamespace',
'StripPrefixNamespace', 'TokenizeIdentifier', '_IsValidPathStringResult',
'__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instance_size__', '__le__', '__lt__', '__module__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', 'absoluteIndicator', 'absoluteRootPath', 'childDelimiter', 'elementString', 'emptyPath', 'expressionIndicator', 'isEmpty',
'mapperArgDelimiter', 'mapperIndicator', 'menvaEnd', 'menvaStart', 'name', 'namespaceDelimiter', 'parentPathElement',
'pathElementCount', 'pathString', 'propertyDelimiter', 'reflexiveRelativePath', 'relationshipTargetEnd', 'relationshipTargetStart',
'targetPath']
'''

p01 = Sdf.Path("/aa")
p02 = Sdf.Path("/bb")

print(type(p01.GetPrimPath()))
print(p01.pathString)

print(p01.AppendChild('ee'))
print(p01.AppendPath('ae/ee'))