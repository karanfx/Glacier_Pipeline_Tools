import os
import json
import ctypes
import sys
# import runas

tooldir = json.load(open('bin/data/softpaths.json'))

def houdini_def():
    # path = tooldir['Houdini']
    file_path = "C:/Program Files/Side Effects Software/Houdini 18.5.596/houdini/scripts/123.py"
    # path = 'bin/def_scenes/123.py'


    # # Clean path
    # trimmed_path = path[:path.rfind("/")]
    # print(trimmed_path)


    # filename = '123.py'
    def_scene = 'bin/def_scenes/hou_default.hip'
    def_commands = f'hou.hipFile.merge({def_scene})'

    # if ctypes.windll.shell32.IsUserAnAdmin():
    #     return True

    # params = f'"{os.path.abspath(__file__)}"'
    # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    
    # os.umask(0)
    # def opener(path,flags):
    #     return os.open(path,flags,0o777)
    
    # if os.path.isfile(file_path):
    #     with open(file_path,'w',opener=opener) as f:
    #         f.write(def_commands)
    #         print('write')
    
    with open(file_path,'w+') as f:
        f.write(def_commands)
        print('write')
    os.chmod(file_path,0o777)

houdini_def()