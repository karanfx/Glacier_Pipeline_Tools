# # import pxr.Usdview 
# import os
# cur_shot = os.environ("SHOT")
# print(cur_shot)

# print('Launch through subprocess')
vers = "v002"
# n_vers = vers + 1


# v = "\"safdfs\""
# print(v)
# print(v.strip("\""))

prog = "C:/Program Files/Nuke14.0v1/Nuke14.0.exe"
script = "E:/Work/python_dev/QT_project_launcher/utils/nuke/slapcomp.py"

import subprocess
# subprocess.run([prog,script],shell=True)

import os
os.startfile([prog+script])