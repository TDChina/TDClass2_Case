#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Sat Oct 27 21:01:55 2018
#========================================
import maya.OpenMaya as OpenMaya
import pymel.core as pm 
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

iterator = OpenMaya.MItDependencyGraph(pm.PyNode('Mery_preview_lips_shaderSG').__apimobject__())

while not iterator.isDone():
    iterator.next()



node = OpenMaya.MFnDependencyNode()
node.create('transform')
node.setName('test')



ball = pm.PyNode('pSphere1').__apimobject__()
node = OpenMaya.MFnDependencyNode(ball)
node.setName('qiu')



top_group = pm.PyNode('Mery_hair_offset_preview_grp').__apiobject__()
node = OpenMaya.MFnDagNode(top_group)
node.fullPathName()
node.partialPathName()



# 找到场景内的 SG 节点
selction = OpenMaya.MSelectionList()
iterator = OpenMaya.MItDependencyNodes(OpenMaya.MFn.kShadingEngine)
while not iterator.isDone():
    selction.add(iterator.item())
    iterator.next()
selction.length()



# 获取所有的 多边形节点
iterator = OpenMaya.MItDag(OpenMaya.MItDag.kDepthFirst, OpenMaya.MFn.kMesh)

while not iterator.isDone():
    print iterator.fullPathName()
    iterator.next()


    
# 找出节点下游节点
iterator = OpenMaya.MItDependencyGraph(pm.PyNode('Mery_preview_lips_shaderSG').__apimobject__())

while not iterator.isDone():
    print OpenMaya.MFnDependencyNode(iterator.currentItem()).name()
    iterator.next()

