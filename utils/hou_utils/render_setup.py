import hou

for node in hou.selectedNodes():
    path = node.path()
    #print(path)
    #get node names
    name = path.split("/")
    render_name = "mantra" + name[-1]
    mat_name = "shader" + name[-1]
    geo_name = "RNDR_" + name[-1]
    
    #create geo/objectmerge node 
    obj = hou.node("/obj")
    geo_node = obj.createNode("geo",geo_name)
    object_merge_node = geo_node.createNode("object_merge",(geo_name + "_object_merge"))
    #add object
    object_merge_node.parm("objpath1").set(path)
    #add output node
    output_node = geo_node.createNode("output","OUTPUT")
    output_node.setInput(0,object_merge_node,0)
    
    #create render node
    out = hou.node("/out")
    render_node = out.createNode("ifd",render_name)
    #pick render objects
    render_node.parm("forceobject").set(geo_node.path())

    render_node.parm("trange").set(1)
    render_node.parm("vm_renderengine").set(3)
    render_node.parm("f1").setExpression("$FSTART")
    render_node.parm("f2").setExpression("$FEND")
    
    #create material
    mat = hou.node("/mat")
    mat_node = mat.createNode("principledshader::2.0",mat_name)
    #assign material
    geo_node.parm("shop_materialpath").set(mat_node.path())
    