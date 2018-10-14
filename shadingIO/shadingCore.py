#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Sun Oct 14 20:13:01 2018
#========================================
import maya.cmds as mc
import json
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_all_sg_nodes():
    '''
    '''
    sg_nodes = mc.ls(typ='shadingEngine')
    return sg_nodes



def get_sel_sg_nodes():
    '''
    '''
    sg_nodes = list()
    selected_geos = mc.ls(sl=True)
    for geo in selected_geos:
        shapes = mc.listRelatives(geo, children=True, path=True) or list()
        for shp in shapes:
            sg_node = mc.listConnections(shp, destination=True, t='shadingEngine')
            sg_nodes.extend(sg_node)
    
    sg_nodes = [sg for i, sg in enumerate(sg_nodes) if sg not in sg_nodes[:i]]
    return sg_nodes




def export_sg_nodes(sg_nodes, file_path):
    '''
    '''
    if len(sg_nodes) == 0:
        return False
    
    mc.select(sg_nodes, r=True, ne=True)
    mc.file(file_path, options="v=0;", typ="mayaAscii", pr=True, es=True)
    return True



def export_all_sg_nodes(file_path):
    '''
    '''
    return export_sg_nodes(get_all_sg_nodes(), file_path)




def export_sel_sg_nodes(file_path):
    '''
    '''
    return export_sg_nodes(get_sel_sg_nodes(), file_path)



def get_all_sg_members():
    '''
    '''
    data = dict()
    for sg in get_all_sg_nodes():
        members = mc.sets(sg, q=True)
        data[sg] = members
    return data



def get_sel_sg_members():
    '''
    '''
    data = dict()
    for sg in get_sel_sg_nodes():
        members = mc.sets(sg, q=True)
        data[sg] = members
    return data



def export_sg_members(data, file_path):
    '''
    '''
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    return True



def export_all_sg_members(file_path):
    '''
    '''
    return export_sg_members(get_all_sg_members(), file_path)



def export_sel_sg_members(file_path):
    '''
    '''
    return export_sg_members(get_sel_sg_members(), file_path)
