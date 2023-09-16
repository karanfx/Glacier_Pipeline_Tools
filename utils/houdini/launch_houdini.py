def setup_env(self):
        env_file = "C:/Users/PERMAN/Documents/houdini18.5/houdini.env"
        search_text = "# Glacier Variables"
        num_var = 6
        
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

        # print(f"Deleted {num_var} lines after each occurrence of '{search_text}'.")
        
        #Setup Variables
        toolname = self.tools_cB.currentText()
        proj = self.project_cB.currentText()
        seq = self.seq_cB.currentText()
        shot = self.shot_cB.currentText()
        shot_dir = self.manual_path_Ldit.text()
        shot_dir = shot_dir.replace("\\","/")

        job = os.path.join(shot_dir,toolname)

        #Set env variables

        variables = {"SHOW" : proj, "SEQ": seq, "SHOT":shot,"SHOT_DIR":shot_dir,"JOB":job}
        with open(env_file,"a") as env:
            env.write("# Glacier Variables\n")
            for var,data in variables.items():
                env.write(var +"="+ "\"" + data + "/" + "\"" + "\n")


import hou
import os

def set_hou_shot_def(show_name,seq_name,shot_name,user_name,shot_dir,start_frame,end_frame):
    
    # Set a custom environment variable
    variables = { "SHOW": show_name, "SHOT": shot_name,
                "SHOT_DIR":shot_dir,"USER":user_name}


    for var_name,var_val in variables.items():
        # Set the environment variable
        hou.hscript("setenv {}={}".format(var_name, var_val))

        print("Environment variable {} set to: {}".format(var_name, hou.getenv(var_name)))

    #set shot range
    hou.playbar.setFrameRange(start_frame, end_frame)
    hou.setFrame(start_frame)
    # hou.hipFile.save(hou.hipFile.path())
    hou.hipFile.save(os.path.join(shot_dir,"houdini/scene")+"/default.hip")

def launch_version(soft_dir,file_dir):
    import subprocess
    subprocess.Popen([soft_dir, file_dir])