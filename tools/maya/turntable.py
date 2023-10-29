import maya.cmds as cmds

def create_turntable_playblast(output):
    start_frame = 1
    end_frame = 120
    
    #Setup Playbar
    cmds.playbackOptions(edit=True,animationStartTime = start_frame)
    cmds.playbackOptions(edit=True,animationEndTime = end_frame)
    
    cmds.playbackOptions(edit=True,minTime = start_frame)
    cmds.playbackOptions(edit=True,maxTime = end_frame)
    
    
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No object selected. Please select an object.")
        return

    # Center the selected object at the world origin.
    cmds.xform(selected_objects, translation=(0, 0, 0))
    
    bounding_box = cmds.exactWorldBoundingBox(selected_objects)
    max_size = max(bounding_box)
    center_x = bounding_box[3]/4
    center_y = bounding_box[4]/2
    center_z = bounding_box[5]/2 + max_size*3

    # Create a camera.
    camera_name = "turntable_camera"
    if cmds.objExists(camera_name):
        cmds.delete(camera_name)
    camera = cmds.camera(name=camera_name)[0]

    # Set camera xform to +x,z max
    cmds.setAttr(camera + ".translateX", center_x)
    cmds.setAttr(camera + ".translateY", center_y)
    cmds.setAttr(camera + ".translateZ", center_z)

    #Center Group as aim 
    aim_group = cmds.group(empty=True, name='aim_name' + '_group')
    cmds.parent(camera,aim_group)

    # turntable animation
    turntable_anim = cmds.setKeyframe(aim_group, attribute="rotateY", time=start_frame, value=0,  itt='linear', ott='linear')
    cmds.setKeyframe(aim_group, attribute="rotateY", time=end_frame, value=360,itt='linear', ott='linear')
    cmds.select(selected_objects, deselect=True)

    #Take the playblast    
    width = 1024
    height = 1024
   
    cmds.hide()
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
    cmds.showHidden()
    cmds.delete(aim_group)


import os
shot_dir = os.environ["SHOT_DIR"]
shot_name = os.environ["SHOT"]
user = os.environ["USER"]

version_dir = os.path.join(shot_dir,user,"maya","playblast")

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
