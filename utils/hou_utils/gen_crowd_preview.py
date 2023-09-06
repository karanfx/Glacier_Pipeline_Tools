import hou
import os

# #Set Attributes
# char_path = "test"
# anim_path = "test"
# prev_dir = "test"

#Cam setting
trans = (-3.25,1.07,4.97)
rot = (-1.12,-33.69,2.86)

def fbx_preview(char_path,anim_path,prev_dir,trans,rot):
    obj = hou.node("/obj/")
    geo = obj.createNode("geo","fbx_preview")
    #Create nodes
    char_fbx = geo.createNode("kinefx::fbxcharacterimport","import_fbx")
    char_fbx.parm("fbxfile").set(char_path)
    char_fbx.parm("animfbxfile").set(anim_path)

    #Create and connect deform nodes
    deform = geo.createNode("bonedeform","deform_bone")
    deform.setInput(0,char_fbx,0)
    deform.setInput(1,char_fbx,1)
    deform.setInput(2,char_fbx,2)

    deform.setRenderFlag(True)
    deform.setDisplayFlag(True)

    #create Camera
    cam = obj.createNode("cam","preview_cam")

    #set translate and rotate
    cam.parm("tx").set(trans[0])
    cam.parm("ty").set(trans[1])
    cam.parm("tz").set(trans[2])

    cam.parm("rx").set(rot[0])
    cam.parm("ry").set(rot[1])
    cam.parm("rz").set(rot[2])

    cam.parm("resx").set(512)
    cam.parm("resy").set(512)

    hou.playbar.setFrameRange(1,50)
    #Set Opengl nodes
    out = hou.node("/out")
    opengl_node = out.createNode("opengl","opengl_flipbook")
    opengl_node.parm("camera").set(cam.path())
    opengl_node.parm("trange").set(1)
    opengl_node.parm("aamode").set(4)
    opengl_node.parm("f1").setExpression("$FSTART")
    opengl_node.parm("f2").setExpression("$FEND")
    opengl_node.parm("picture").set(prev_dir)
    opengl_node.parm("execute").pressButton()

    #Clear Scene
    opengl_node.addEventCallback((hou.nodeEventType.PostRender, ), hou.hipFile.clear())
    


#set 
crowd_dir = "D:/test_studio/Show01/libs/crowd"
char_path = os.path.join(crowd_dir,"agents")
anim_path = os.path.join(crowd_dir,"anim")

for char in os.listdir(char_path):
    char_dir = os.path.join(char_path,char)
    print(char_dir)
    if char.endswith(".fbx") is True:
        # print(char)
        char_name = char.strip(".fbx")
        # print(char_name)
        clip_dir  = os.path.join(anim_path,char_name)
        print(clip_dir)
        for pack in os.listdir(clip_dir):
            pack = os.path.join(clip_dir,pack)
            # print(pack)

            for clip in os.listdir(pack):
                clip = os.path.join(pack,clip)
                print(clip)

                # fbx_preview(char_dir,clip,prev_dir,trans,rot)