import hou
import os 

shot_dir = os.environ.get('SHOT_DIR')
user = os.environ.get('USER')

version_dir = os.path.join(shot_dir,user,"houdini","flipbook")

def auto_vers(version_dir):
    #Auto version up
    versions = os.listdir(version_dir)

    if versions:
        max_v = str(max(versions))
        max_v = int(max_v.strip('v'))

        max_v += 1
        vers_up = "v{:03d}".format(max_v)

    else:
        vers_up = "v001"
        
    return vers_up

version = auto_vers(version_dir)

out_dir = os.path.join(shot_dir,user,"houdini","flipbook",version)


out = hou.node("out/")
cameras = hou.selectedNodes()
for cam in cameras:
    opengl_node = out.createNode("opengl","opengl_flipbook")
    opengl_node.parm("camera").set(cam.path())
    opengl_node.parm("trange").set(1)
    opengl_node.parm("aamode").set(4)
    opengl_node.parm("f1").setExpression("$FSTART")
    opengl_node.parm("f2").setExpression("$FEND")

    new_param = opengl_node.addSpareParmTuple(hou.IntParmTemplate("vers", "Version", 1, (1,)))
    c_path = "$SHOT_DIR/$USER/houdini/flipbook/`$OS`/v00`chs(\"vers\")`/`$OS`_v00`chs(\"vers\")`_`$F4`.png"

    opengl_node.parm("picture").set(c_path)

    opengl_node.parm("execute").pressButton()