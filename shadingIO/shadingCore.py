#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Sun Oct 14 20:13:01 2018
#========================================
import maya.cmds as mc
import json, os
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




def get_sg_members(sg_nodes=list()):
    '''
    '''
    data = dict()
    for sg in sg_nodes:
        members = mc.sets(sg, q=True) or list()
        filter_members = list()
        for m in members:
            obj = m.split('.')
            if mc.nodeType(obj[0]) != 'transform':
                obj[0] = mc.listRelatives(obj[0], p=True)[0]
            filter_members.append('.'.join(obj))
            
        data[sg] = filter_members
    
    return data



def get_all_sg_members():
    '''
    '''
    return get_sg_members(get_all_sg_nodes())



def get_sel_sg_members():
    '''
    '''
    return get_sg_members(get_sel_sg_nodes())
    


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




def reference_shader_file(file_path):
    '''
    '''
    file_path = file_path.replace('\\', '/')
    ref_files = mc.file(query=True, reference=True)
    if file_path in ref_files:
        return mc.file(file_path, query=True, namespace=True)
    
    name_space = os.path.splitext(os.path.basename(file_path))[0]
    mc.file(file_path, r=True, ns=name_space)
    return name_space



def assign_data_to_all(data_path, sg_namespace=None, geo_namespace=None):
    '''
    '''
    data = dict()
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    for sg, geos in data.items():
        if sg_namespace:
            sg = '{0}:{1}'.format(sg_namespace, sg)
        if not mc.objExists(sg):
            continue
        
        filter_items = list()
        for g in geos:
            g = '{0}:{1}'.format(geo_namespace, g)
            if mc.objExists(g.split('.')[0]):
                filter_items.append(g)
        
        try:
            mc.sets(filter_items, e=True, forceElement=sg)
        except:
            pass
