import os
import hou

def import_fbx(dir):
    ext = os.path.splitext(dir)[1]
    ext = os.path.splitext(dir)[1]
    name = os.path.basename(dir).replace(ext,"")
    if ext == ".fbx":
        fbx_dirs = []
        subnet = hou.hipFile.importFBX(file_name=dir, import_geometry=True)
        print(subnet)
    else:
        pass
    

def import_alembic(dir):
    ext = os.path.splitext(dir)[1]
    name = os.path.basename(dir).replace(ext,"")
    ext = os.path.splitext(dir)[1]
    if ext == ".abc":
        obj = hou.node("obj/")
        target_node = obj.createNode("geo",name)

        alembic_sop = target_node.createNode("alembic",name)
        alembic_sop.parm("fileName").set(dir)
        alembic_sop.cook()
    else:
        pass



def import_usd(dir):
    ext = os.path.splitext(dir)[1]
    name = os.path.basename(dir).replace(ext,"")
    if ext == ".fbx":
        obj = hou.node("stage/")
        sop_import = obj.createNode("sopimport",name)
        sop_import.parm("savepath").set(dir)
        sop_import.cook()
    else:
        pass


layout = "D:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001/layout/"
for sub in os.listdir(layout):
    dirs = os.path.join(layout,sub)
    # print(dirs)
    for asset in os.listdir(dirs):
        asset_dirs = os.path.join(dirs,asset)
        ext = os.path.splitext(asset_dirs)[1]
        name = os.path.basename(asset_dirs).replace(ext,"")
        print(name)

        #call imports
        import_alembic(asset_dirs)
        import_fbx(asset_dirs)
        import_usd(asset_dirs)
        # print(asset_dirs)