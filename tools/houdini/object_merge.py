#create object merge for selected node

import hou

for node in hou.selectedNodes():
    path = node.path()
    #print(path)
    name = path.split("/")
    geo_name = name[-1]
    obj = hou.node("/obj")
    geo_node = obj.createNode("geo",geo_name)
    object_merge_node = geo_node.createNode("object_merge",(geo_name + "_object_merge"))
    object_merge_node.parm("objpath1").set(path)
