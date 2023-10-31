# # import pxr.Usdview 
# import os
# cur_shot = os.environ("SHOT")
# print(cur_shot)

#mail template
# render_name = hou.pwd()

output_nodes = {"filecache":"file","rop_alembic":"filename",
                "opengl":"picture","ifd":"vm_picture","usdexport":"lopoutput",
                "file":"file","usdrender":"outputimage"}

print(output_nodes.get("opengl"))
for node,out in output_nodes.items():
    print(out)
#     if render_name.type().name() == node:
#         output_parm = output_nodes.get(node)
#         print(output_parm)
