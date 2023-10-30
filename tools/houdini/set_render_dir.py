import hou

output_nodes = {"filecache":"file","rop_alembic":"filename",
                 "opengl":"picture","ifd":"vm_picture","usdexport":"lopoutput",
                 "file":"file","usdrender":"outputimage"}

    
for node in hou.selectedNodes():
    for type,out_path in output_nodes.items():
        # print(type,out_path)
        if node.type().name() == type:
            # if node.parm("file") is None:
            new_param = node.addSpareParmTuple(hou.IntParmTemplate("vers", "Version", 1, (1,)))

            c_path = "$SHOT_DIR/$USER/houdini/cache/`$OS`/v00`chs(\"vers\")`/`$OS`_v00`chs(\"vers\")`.`$F4`.bgeo.sc"
            r_path = "$SHOT_DIR/$USER/houdini/renders/`$OS`/v00`chs(\"vers\")`/`$OS`_v00`chs(\"vers\")`.`$F4`.png"

            if type == 'ifd':
                node.parm(out_path).set(r_path)
            else:
                node.parm(out_path).set(c_path)
        else:
            # print("Not Correct Node")
            # hou.ui.displayMessage("Please, Select Export/OUT node",title = "Glacier Tools")
            pass