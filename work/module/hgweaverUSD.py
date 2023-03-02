from pxr import Usd, UsdUtils, Sdf, UsdShade, UsdGeom
import maya.cmds as cmds
import os

arnold_options_template = "-boundingBox;-exportAllShadingGroups;-mask {USD_MASK};-lightLinks 0;-shadowLinks 0;-expandProcedurals;-fullPath"


def export_selected(file_path, step='') -> str:
    global arnold_options_template
    if step == '':
        return
    step = step.lower()

    usd_mask = 0
    if step == 'mdl':
        usd_mask = '8'
    elif step == 'ldv':
        usd_mask = '2224'

    arnold_options = arnold_options_template.format(USD_MASK=usd_mask)
    cmds.file(file_path, f=True, options=arnold_options, typ='Arnold-USD', pr=True, es=True)

    return file_path






def make_stage(_path='', typ='NORMAL'):
    if typ == 'MEMORY':
        if os.path.exists(_path):
            return Usd.Stage.CreateInMemory(_path)
        else:
            return Usd.Stage.CreateInMemory()

    if os.path.exists(_path):
        _main_stage  = Usd.Stage.Open(_path)
    else:
        _main_stage  = Usd.Stage.CreateNew(_path)

    return _main_stage


def open_stage(_path :str="") -> Usd.Stage:
    if os.path.exists(_path) == False:
        return None
    return Usd.Stage.Open(_path)




def get_material_prim(_stage, _prim_path):
    return UsdShade.Shader.Material(_stage, _prim_path)



def get_shader_prim(_stage, _prim_path):
    return UsdShade.Shader.Get(_stage, _prim_path)





def get_connected_output_sdfpath(_prim):
    _res = []
    for _output in _prim.GetOutputs():
        _output_basename = _output.GetBaseName()
        _connected_res = _output.GetRawConnectedSourcePaths()
        if _connected_res == []:
            continue

        _src_path = _connected_res[0].pathString


        _res.append((_output, _output_basename, _src_path))

    return _res



def get_connected_input_sdfpath(_prim):
    _res = []
    for _input in _prim.GetInputs():
        _input_basename = _input.GetBaseName()
        _connected_res = _input.GetRawConnectedSourcePaths()
        if _connected_res == []:
            continue

        _src_path = _connected_res[0].pathString


        _res.append((_input, _input_basename, _src_path))

    return _res









def set_STR(_stage, _tar_prim, str_info):
    _check_prop_list = _tar_prim.GetPropertyNames()
    for _property_name, _prop_value in str_info.items():
        if _property_name in _check_prop_list:
            continue
        tar_xform_prim = UsdGeom.Xform.Get(_stage, _tar_prim.GetPath())
        if _property_name == 'xformOp:translate':
            tar_xform_prim.AddTranslateOp()
            _tar_prim.GetProperty('xformOp:translate').Set(_prop_value)
        elif _property_name == 'xformOp:scale':
            tar_xform_prim.AddScaleOp()
            _tar_prim.GetProperty('xformOp:scale').Set(_prop_value)
        elif _property_name == 'xformOp:rotateXYZ':
            tar_xform_prim.AddRotateXYZOp()
            _tar_prim.GetProperty('xformOp:rotateXYZ').Set(_prop_value)




def add_reference(_stage, prim_path, usd_file_path, usd_file_default_prim='',str_info={}):
    if usd_file_default_prim == '':
        usd_file_default_prim_path = make_stage(usd_file_path).GetDefaultPrim().GetPath()
        print(usd_file_default_prim_path)
        print(type(usd_file_default_prim_path))

    defined_prim = _stage.DefinePrim(prim_path, 'Xform')
    defined_prim.GetReferences().AddReference(usd_file_path, usd_file_default_prim_path)

    if str_info != {}:
        set_STR(_stage, defined_prim, str_info)






def stage_from_file(_path :str) -> str:
    if os.path.exists(_path) == False:
        return
    
    fname           = os.path.basename(_path)
    grp_name, _ext  = os.path.splitext(fname)
    node_name       = grp_name + "Shape"



    if cmds.objExists(grp_name) == True:
        cmds.delete(grp_name)
        
    created_node = cmds.createNode("mayaUsdProxyShape", n=node_name, p=grp_name)
    cmds.setAttr(created_node + ".filePath", _path, type="string")

















































def is_with_namespace(_tar):
    if ':' in _tar:
        return True
    else:
        return False



def is_top_node(tar_node):
    element_list = tar_node.split('|')
    if len(element_list) == 2:
        return True
    else:
        return False




def get_targets(all_info_dict):
    all_tars = cmds.ls(sl=True, l=True)

    for _tar in all_tars:
        _each_asset_dict = {}
        _with_ns = False
        _is_top = False
        _parent_address = ''


        if is_with_namespace(_tar) == True:
            _with_ns = True
        else:
            _with_ns = False


        if is_top_node(_tar) == True:
            _is_top = True
        else:
            _is_top = False
            _temp = _tar.split('|')
            _temp.pop()
            _parent_address = '|'.join(_temp)

        all_info_dict[_tar] = {'IS_TOP':_is_top, 'PARENT_ADDRESS':_parent_address, 'NAMESPACE':_with_ns}

    return all_info_dict












def get_all_shape_in_hierarchy(grp=None):
    if grp is None:
        grp = cmds.ls(sl=True)[0]

    return cmds.listRelatives(grp, ad=True, f=True, typ = 'shape')



def get_shading_engines(shape):
    # return cmds.listConnections (shape, source=False, destination=True)
    connected_list = cmds.listConnections (shape, source=False, destination=True)

    result_shading_engine_list = []
    if connected_list == None:
        return None
    else:
        for node in connected_list:
            node_type = cmds.nodeType(node)
            if node_type == 'shadingEngine':
                result_shading_engine_list.append(node)
        return result_shading_engine_list



def get_shading_groups_in_hierarchy(grp):
    shading_engine_list = []

    for shape in get_all_shape_in_hierarchy(grp):
        shading_engines = get_shading_engines(shape)
        if not shading_engines == None:
            check_engines_list = shading_engines
            while 'initialShadingGroup' in check_engines_list:
                shading_engines.remove('initialShadingGroup')
            if not shading_engines:
                continue
            else:
                for _shadinggroup in shading_engines:
                    if not _shadinggroup in shading_engine_list:
                        shading_engine_list.append(_shadinggroup)

            # print '{0} -----------------------> '.format(shape)
            # print shading_engines

    return shading_engine_list








def make_magic_path(f_path):
    _temp = f_path.split(':')[-1]
    if ':' in f_path:
        return '*:*{0}*'.format(_temp)
    else:
        return '*{0}*'.format(_temp)



def get_geom(sg):
    members = cmds.sets(sg, q=True)
    paths = []
    for member in members:
        _IS_ATTRIBUTE = False

        if '.f' in member:
            _IS_ATTRIBUTE = True
        else:
            _IS_ATTRIBUTE = False


        if _IS_ATTRIBUTE == False:
            # full_path = cmds.listRelatives(member, fullPath=True, allParents=True).pop()
            full_path = cmds.listRelatives(member, allParents=True, f=True).pop()
        else:
            full_path = cmds.ls(member, l=True).pop()
            # full_path = cmds.ls(member).pop()

        # print(full_path)
        # magic_path = make_magic_path(full_path)
        full_path = full_path.replace('|', '/')
        paths.append(full_path)

    return list(set(paths))






def get_mat(_sg):
    all_linked_node = cmds.listConnections(_sg, d=False, s=True)
    linked_mat = cmds.ls(all_linked_node, mat=True)

    if linked_mat is None or linked_mat == []:
        return ''
    return linked_mat[0]







def get_assigned_info():
    all_info_dict = {}
    all_info_dict = get_targets(all_info_dict)

    export_tar_sg_list = []
    for _tar, _tar_info_dict in all_info_dict.items():
        sg_list = get_shading_groups_in_hierarchy(_tar)
        export_tar_sg_list.extend(sg_list)

        link_info_dict = {}
        for _sg in sg_list:
            assigned_shapes = get_geom(_sg)
            assigned_mat = get_mat(_sg)
            # link_info_dict[_sg] = assigned_shapes
            link_info_dict[assigned_mat] = assigned_shapes

        _tar_info_dict['LINK'] = link_info_dict

    return (list(all_info_dict.values()).pop()).get('LINK')
