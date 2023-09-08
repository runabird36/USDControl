def _get_root(node, predicate=None):
    """Find the top-most DAG node.

    Args:
        node (str): A Maya node to get the root node of.

    Returns:
        str: The found Maya node. If `node` is the root then it is returned.

    """
    parents = cmds.listRelatives(node, fullPath=True, parent=True) or []
    parents = [parent for parent in parents if predicate(parent)]

    if parents:
        return _get_root(parents[0], predicate=predicate)

    return node

def convert_maya_path_to_usd(path):
    """Change an absolute Maya node path into a USD SdfPath-style path.

    Args:
        path (str): Some path like "|group1|pSphere1|pSphereShape1".

    Returns:
        str: The converted USD path. e.g. "/group1/pSphere1/pSphereShape1".

    """
    path = path.replace("|", "/")

    return path
    
def _get_relative_joint_path(joint, root):
    """Get a Maya node path that is relative to some root Maya node.

    This function is mainly so that we can convert an absolute Maya joint path
    into a relative path rooted as a UsdSkelRoot.

    Args:
        joint (str):
            Some absolute joint path.
            e.g. "|group1|root_joint|foo|bar|some_joint".
        root (str):
            The absolute path to the first joint in a joint hierarchy.
            e.g. "|group1|root_joint"

    Returns:
        str: The UsdSkelRoot-relative path to a Maya joint. This path
             is not meant to be a valid Maya DAG path but a path that can later be
             converted to a USD-joint path.
             e.g. "root_joint|foo|bar|some_joint".

    """
    root_node_name = cmds.ls(root, shortNames=True)[0]

    if joint == root:
        return root_node_name

    return root_node_name + "|" + joint[len(root) + 1 :]

def _convert_to_usd_joint_syntax(joints):
    """Change an entire Maya joint hierarchy into a valid USD hierarchy.

    Args:
        joints (iter[str]):
            The absolute path to a Maya joint hierarchy to convert.
            It's recommended to give all joints in a joint hierarchy
            to this function, to make sure the joints will have the
            right topology order.

    Returns:
        tuple[list[str], list[str]]:
            The converted USD joint paths and the re-ordered Maya joint paths.

    """
    return [convert_maya_path_to_usd(joint).lstrip("/") for joint in joints]



def get_all_joints(joint):
    """Get the full joint hierarchy that `joint` is a part of.

    Note:
        This function will include the top-level root joint that `joint` is
        usually a part of.

    Args:
        joint (str): The path to a Maya node.

    Returns:
        list[str]: Every joint in the entire joint hierarchy. This list
            also includes the root joint node.

    """

    def _is_joint(node):
        return cmds.nodeType(node) == "joint"

    root = cmds.ls(_get_root(joint, predicate=_is_joint), long=True)[0]
    joints = cmds.listRelatives(root, allDescendents=True, fullPath=True) or []

    root_node_name = cmds.ls(root, shortNames=True)[0]

    # The UsdSkel documentation requires that joints are written parents
    # first, then children. This is easy to do in Maya - just sort the
    # joints and then it will be in the correct order.
    #
    topology = sorted(joints)

    usd_topology = _convert_to_usd_joint_syntax(
        [root_node_name] + [_get_relative_joint_path(joint, root) for joint in topology]
    )

    return (usd_topology, [root] + topology)

def get_connected_meshes(joint):
    """Find every mesh that is skinned for some joint.

    Note:
        This function only works for Maya skin clusters.

    Args:
        str (str): The name of some Maya joint that is skinned to 1+ Maya mesh.

    Returns:
        set[str]: The Maya meshes that `joint` affects.

    """
    clusters = set(
        node
        for node in cmds.listConnections(joint, destination=True) or []
        if cmds.nodeType(node) == "skinCluster"
    )

    meshes = set()

    for cluster in clusters:
        for node in cmds.listConnections(cluster + ".outputGeometry", destination=True):
            node = cmds.ls(node, long=True)[0]  # Force the full path to the node
            meshes.add(node)

    return meshes
    
jnt_root = "Root_M"
joints, nodes = get_all_joints(jnt_root)
    
meshes = set(mesh for joint in nodes for mesh in get_connected_meshes(joint))

from pprint import pprint
#pprint(meshes)
#pprint(joints)
#pprint(nodes)
def get_overall_bounding_box(meshes, time_code):
    """Find a bounding box that surrounds every given Maya mesh.

    Args:
        meshes (list[str]): The paths to Maya meshes that each have bounding box data.
        time_code (float or int): The time to get bounding box data for.

    Raises:
        ValueError: If `meshes` is empty.

    Returns:
        tuple[tuple[float, float, float], tuple[float, float, float]]:
            The two 3D points that surround the bounding boxes of every given mesh.

    """
    if not meshes:
        return ValueError('Meshes "{meshes}" cannot be empty.'.format(meshes=meshes))

    minimum_x_values = set()
    minimum_y_values = set()
    minimum_z_values = set()
    maximum_x_values = set()
    maximum_y_values = set()
    maximum_z_values = set()

    for mesh in meshes:
        minimum_x_values.add(cmds.getAttr(mesh + ".boundingBoxMinX", time=time_code))
        minimum_y_values.add(cmds.getAttr(mesh + ".boundingBoxMinY", time=time_code))
        minimum_z_values.add(cmds.getAttr(mesh + ".boundingBoxMinZ", time=time_code))

        maximum_x_values.add(cmds.getAttr(mesh + ".boundingBoxMaxX", time=time_code))
        maximum_y_values.add(cmds.getAttr(mesh + ".boundingBoxMaxY", time=time_code))
        maximum_z_values.add(cmds.getAttr(mesh + ".boundingBoxMaxZ", time=time_code))

    minimum_x = sorted(minimum_x_values)[0]
    minimum_y = sorted(minimum_y_values)[0]
    minimum_z = sorted(minimum_z_values)[0]
    maximum_x = sorted(maximum_x_values)[0]
    maximum_y = sorted(maximum_y_values)[0]
    maximum_z = sorted(maximum_z_values)[0]

    return (
        (minimum_x, minimum_y, minimum_z),
        (maximum_x, maximum_y, maximum_z),
    )
    
    
times = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0]

for time_code in times:
    bounding_box = [
        Gf.Vec3f(*point)
        for point in get_overall_bounding_box(meshes, time_code)
    ]
    pprint(bounding_box)