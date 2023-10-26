import maya.cmds as cmds

def create_turntable_playblast():
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No object selected. Please select an object.")
        return

    # Center the selected object at the world origin.
    cmds.xform(selected_objects, translation=(0, 0, 0))
    
    bounding_box = cmds.exactWorldBoundingBox(selected_objects)
    center_x = (bounding_box[0] + bounding_box[3])
    center_y = (bounding_box[1] + bounding_box[4])
    center_z = (bounding_box[2] + bounding_box[5]) 

    # Create a camera.
    camera_name = "turntable_camera"
    if cmds.objExists(camera_name):
        cmds.delete(camera_name)
    camera = cmds.camera(name=camera_name)[0]

    # Set camera attributes (adjust these values as needed).
    cmds.setAttr(camera + ".translateX", center_x)
    cmds.setAttr(camera + ".translateY", center_y)
    cmds.setAttr(camera + ".translateZ", bounding_box[5] + 10)
    cmds.setAttr(camera + ".rotateX", -30)
    cmds.setAttr(camera + ".rotateY", 0)
    cmds.setAttr(camera + ".rotateZ", 0)

    # Set up the turntable animation.
    turntable_anim = cmds.setKeyframe(camera, attribute="rotateY", time=1, value=0)
    cmds.setKeyframe(camera, attribute="rotateY", time=120, value=360)
    cmds.select(selected_objects, deselect=True)
    cmds.hide()
    cmds.currentTime(1)
    cmds.playblast(format="qt", filename="turntable_playblast.mov",quality=100, forceOverwrite=True, showOrnaments=False)

    # Clean up.
    cmds.showHidden()
    cmds.delete(turntable_anim)
    cmds.delete(camera)

# Run the function.
create_turntable_playblast()
