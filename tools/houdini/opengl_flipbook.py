import hou

out = hou.node("out/")
cameras = hou.selectedNodes()
for cam in cameras:
    opengl_node = out.createNode("opengl","opengl_flipbook")
    opengl_node.parm("camera").set(cam.path())
    opengl_node.parm("trange").set(1)
    opengl_node.parm("aamode").set(4)
    opengl_node.parm("f1").setExpression("$FSTART")
    opengl_node.parm("f2").setExpression("$FEND")
    opengl_node.parm("execute").pressButton()