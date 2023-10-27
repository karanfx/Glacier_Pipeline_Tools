import maya.cmds as cmds

def create_turntable_playblast(output):
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No object selected. Please select an object.")
        return

    # Center the selected object at the world origin.
    cmds.xform(selected_objects, translation=(0, 0, 0))
    
    bounding_box = cmds.exactWorldBoundingBox(selected_objects)
    
    center_x = (bounding_box[3])/2
    center_y = (bounding_box[4])/2
    center_z = (bounding_box[5])*4

    # Create a camera.
    camera_name = "turntable_camera"
    if cmds.objExists(camera_name):
        cmds.delete(camera_name)
    camera = cmds.camera(name=camera_name)[0]

    # Set camera attributes (adjust these values as needed).
    cmds.setAttr(camera + ".translateX", center_x)
    cmds.setAttr(camera + ".translateY", center_y)
    cmds.setAttr(camera + ".translateZ", center_z)

    #Center Group
    aim_group = cmds.group(empty=True, name='aim_name' + '_group')
    cmds.parent(camera,aim_group)

    # Set up the turntable animation.
    turntable_anim = cmds.setKeyframe(aim_group, attribute="rotateY", time=1, value=0,  itt='linear', ott='linear')
    cmds.setKeyframe(aim_group, attribute="rotateY", time=120, value=360,itt='linear', ott='linear')
    cmds.select(selected_objects, deselect=True)
    
    # Set the resolution attributes in the render settings.
    width = 1024
    height = 1024
   
    #cmds.hide()
    cmds.currentTime(1)
    cmds.lookThru(camera)
    cmds.playblast(format="avi",
               filename=output,
               forceOverwrite=True,
               clearCache=True,
               viewer=True,
               showOrnaments=True,
               offScreen=True,
               quality=100,
               width=width,  
               height=height)  
               
    # Clean up.
    #cmds.showHidden()
    cmds.delete(aim_group)
    #cmds.delete(camera)


import os
shot_dir = os.environ["SHOT_DIR"]
shot_name = os.environ["SHOT"]


version_dir = os.path.join(shot_dir,"maya","playblast")

#Auto version up
versions = os.listdir(version_dir)


if versions:
    max_v = str(max(versions))
    max_v = int(max_v.strip('v'))

    max_v += 1
    vers_up = "v{:03d}".format(max_v)

else:
    vers_up = "v001"
    
file_name = shot_name + "_" + vers_up + '.avi'
output_dir = os.path.join(version_dir,vers_up,file_name)


create_turntable_playblast(output_dir)
