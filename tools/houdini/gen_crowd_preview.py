# import hou
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



#Another Version of fbx capture
import os
import hou

def captureFbx(fbxPath, cameraDistance=350):

    
    # fbx_dir = os.path.join(fbxPath,fbx)
    par_dir = os.path.dirname(os.path.dirname(fbxPath))
    import pprint
    pprint.pprint(par_dir)
    # Import fbx
    subnet = hou.hipFile.importFBX(file_name=fbxPath, import_geometry=True)
    subnet = subnet[0]

    sub_name = subnet.name()
    
    
    print(sub_name)
    flpbk_dir = os.path.join(par_dir,sub_name,"render")
    pprint.pprint(fbxPath)


    # # Turn off joint viz
    # for node in subnet.children():
    #     if 'bone' in node.name():
    #         node.setDisplayFlag(0)

    # Get main joint (usually Hips)
    rootJntNode = ''
    for node in subnet.children():
        if 'Hips' in node.name():
            rootJntNode = node
            break


    # Create camera and constrain to fbx
    if rootJntNode:
        mainJntTxPath = rootJntNode.parm('tx').path()
        mainJntTyHieght = rootJntNode.parm('ty').eval()
        mainJntTzPath = rootJntNode.parm('tz').path()

        cam = hou.node('/obj').createNode('cam')
        cam.parm('tx').setExpression('ch("%s") + %d' % (mainJntTxPath, int(cameraDistance)))
        cam.parm('ty').set(mainJntTyHieght)
        cam.parm('tz').setExpression('ch("%s") + %d' % (mainJntTzPath, int(cameraDistance)))
        cam.parm('ry').set(45)

        # Add openGL
        openGl =  hou.node('/out').createNode('opengl')

        hou.playbar.setFrameRange(1,50)
        # set frame range
        openGl.parm('trange').set(1)
        frameRange = hou.playbar.playbackRange()
        openGl.parm('/out/opengl1/f1').set(frameRange[0])
        openGl.parm('/out/opengl1/f2').set(frameRange[1])

        # set fbx path as comment
        openGl.parm('/out/opengl1/vpcomment').set(fbxPath)
        openGl.parm('/out/opengl1/tres').set(1)
        openGl.parmTuple('/out/opengl1/res').set((720, 720))


        # make images path
        out_name = sub_name + ".$F4.jpeg"
        outputPath = os.path.join(flpbk_dir,out_name).replace("\\","/")
        openGl.parm('/out/opengl1/picture').set(outputPath)

        openGl.parm('aamode').set(3)
        openGl.parm('/out/opengl1/shadingmode').set(0)
        openGl.parm('/out/opengl1/execute').pressButton()

        
fbxPath = "D:/test_studio/Show01/libs/crowd/character/fbx/draw sword 1.fbx"
fbx_dirs = "D:/test_studio/Show01/libs/crowd/character/fbx/"


# # fbx_dir = os.path.join(fbx_dirs,fbx)
# par_dir = os.path.dirname(os.path.dirname(fbx_dirs))
# import pprint
# # pprint.pprint(fbx_dir)
# pprint.pprint(par_dir)

captureFbx(fbxPath, cameraDistance=350)