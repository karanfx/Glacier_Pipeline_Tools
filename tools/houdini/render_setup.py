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
    geo_node.setColor(hou.Color((1.0,0.25,0.25)))
    object_merge_node = geo_node.createNode("object_merge",(geo_name + "_object_merge"))
    
    geo_node.moveToGoodPosition()
    #add object
    object_merge_node.parm("objpath1").set(path)
    #add output node
    output_node = geo_node.createNode("output","OUTPUT")
    output_node.setInput(0,object_merge_node,0)
    output_node.moveToGoodPosition()

    #Move in network box
    render_netbox = hou.node("/obj/__netbox3")
    if render_netbox:
        render_netbox.addItem(geo_node)
    

    #create render node
    out = hou.node("/out")
    render_node = out.createNode("ifd",render_name)

    # render_node.parm("glstyle").set(1)
    #pick render objects

    #set cam
    children = obj.allSubChildren()
    for child in children:

        if child.type().name() == "camera":
            print(child.name())
            render_node.parm("camera").set(child.name())

        else:
            render_node.parm("camera").set("/obj/cam2")

    #Setup Render Object
    render_node.parm("forceobject").set(geo_node.path())
    render_node.parm("vobject").set("")

    render_node.parm("vm_renderengine").set("physically_based")
    render_node.parm("allowmotionblur").set(1)


    render_node.parm("trange").set(1)
    #render_node.parm("vm_renderengine").set(3)
    render_node.parm("f1").setExpression("$FSTART")
    render_node.parm("f2").setExpression("$FEND")
    
    #create material
    mat = hou.node("/mat")
    mat_node = mat.createNode("principledshader::2.0",mat_name)
    #assign material
    geo_node.parm("shop_materialpath").set(mat_node.path())
    