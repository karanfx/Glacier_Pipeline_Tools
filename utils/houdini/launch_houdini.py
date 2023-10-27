# import hou
import os


#SetUp ENV Variables hard coded
def setup_env(toolname,username,proj,seq,shot,task,shot_dir,start_frame=1001,end_frame=1200):
        env_file = "C:/Users/PERMAN/Documents/houdini18.5/houdini.env"
        search_text = "# Glacier Variables"
        num_var = 10
        
        #Cleanup the file
        # Read the file content into a list of lines
        with open(env_file, 'r') as file:
            lines = file.readlines()

        # Create an empty list to store the modified content
        modified_lines = []

        i = 0
        while i < len(lines):
            line = lines[i]
            if search_text in line:
                # Found the search text, add it to the modified content
                modified_lines.append(line)
                # Skip the next lines_to_delete lines
                for _ in range(num_var):
                    i += 1
            else:
                modified_lines.append(line)
            i += 1
        # Write the modified content back to the file
        with open(env_file, 'w') as file:
            file.writelines(modified_lines)


       #Write ENV VARIABLES
        job = os.path.join(shot_dir,toolname)

        variables = {"USER":str(username),"SHOW" : str(proj), "SEQ": str(seq), "SHOT":str(shot),"SHOT_DIR": str(shot_dir),
                     "JOB":str(job),"TASK":str(task),"G_START": str(start_frame),"G_END": str(end_frame)}
        with open(env_file,"a") as env:
            env.write("# Glacier Variables\n")
            for var,data in variables.items():
                env_format = var +"="+ "\"" + data + "\"" + "\n"
                env.write(env_format)
                # print(env_format)
                


#TEST OUT CLI 
# if toolname == "Houdini_CLI":
#     #open def scene
#     command = tooldata[toolname]
#     # print(command)
#     command += "hscript E:/Work/python_dev/QT_project_launcher/bin/def_scenes/hou_default.hip"
#     #set variables 
#     from utils.houdini.set_shot_def import set_hou_shot_def
#     set_hou_shot_def(proj,seq,shot,username,shot_dir,1001,1200)

#     command += 'hython -c "import sys; sys.path.append("E:/Work/python_dev/QT_project_launcher/utils/hou_utils/");'
#     command += 'import set_hou_shot_def; set_hou_shot_def(proj,seq,shot,username,shot_dir,1001,1200)'
#     # command += "python E:/Work/python_dev/QT_project_launcher/utils/hou_utils/set_shot_def.py"
#     #save scene in shot dir

#     os.system(command)