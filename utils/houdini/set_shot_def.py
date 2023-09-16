# To DO:
# Setup Default scene -almost done
# Load custom tools 
# Setup project directories -done
# Setup Frame Range - done
# Auto-Load Assets
# gather assets

#CLI TOOLS CMDS
# hscript E:\Work\python_dev\QT_project_launcher\bin\def_scenes\hou_default.hip
# python E:/Work/python_dev/QT_project_launcher/utils/hou_utils/set_shot_def.py
# python -c 'hou.hipFile.save(hou.hipFile.path())'

# quit

#set self with HOUDINI_TOOLBAR_PATH in env file


import hou
import os
# start_frame = 1
# end_frame = 100
# show_name = "Show01"
# shot_name = "Shot_AB01"
# user_name = "perman"
# shot_dir = show_name + "/" + shot_name + "/" + user_name

def set_hou_shot_def(show_name,seq_name,shot_name,user_name,shot_dir,start_frame,end_frame):
    
    # Set a custom environment variable
    variables = { "SHOW": show_name, "SHOT": shot_name,
                "SHOT_DIR":shot_dir,"USER":user_name}


    for var_name,var_val in variables.items():
        # Set the environment variable
        hou.hscript("setenv {}={}".format(var_name, var_val))

        # print("Environment variable {} set to: {}".format(var_name, hou.getenv(var_name)))

    #set shot range
    hou.playbar.setFrameRange(start_frame, end_frame)
    hou.setFrame(start_frame)
    # hou.hipFile.save(hou.hipFile.path())
    hou.hipFile.save(os.path.join(shot_dir,"houdini/scene")+"/default.hip")
