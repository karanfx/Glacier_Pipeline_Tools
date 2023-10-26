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

# #setup variables
# def setvar():
#     import os
#     os.environ['SHOT_DIR'] = 'SHOT_setdir'

# import subprocess
# subprocess.run([prog,setvar()],shell=True)

# import os
# os.startfile([prog+script])

import subprocess
import os

envvar = "custom_var_ref"
envvar2 = "custom_var_ref_second"

# Define the custom environment variables
custom_env = {
    "MY_CUSTOM_VARIABLE": envvar,
    "ANOTHER_VARIABLE": envvar2 }

# Launch Nuke with the custom environment variables
nuke_executable = "C:/Program Files/Nuke14.0v1/Nuke14.0.exe"  # Replace with the actual path to your Nuke executable
subprocess.Popen([nuke_executable], env={**os.environ, **custom_env})

def testfunc():
    testvar1 = 32424
    testvar2 = "etsuyfsfd"
    testvar3 = "afbksdnakn"
    return testvar1, testvar2, testvar3

print(testfunc())