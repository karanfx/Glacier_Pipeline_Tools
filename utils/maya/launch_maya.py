def launch_version(soft_dir,file_dir):
    import subprocess
    subprocess.Popen([soft_dir, file_dir])


def setup_env(toolname,username,proj,seq,shot,task,shot_dir,start_frame=1001,end_frame=1200):
    import os
    import maya.cmds as cmds
    job = os.path.join(shot_dir,toolname)

    variables = {"USER":str(username),"SHOW" : str(proj), "SEQ": str(seq), "SHOT":str(shot),"SHOT_DIR": str(shot_dir),
                     "JOB":str(job),"TASK":str(task),"G_START": str(start_frame),"G_END": str(end_frame)}

    for var,data in variables.items():    
        os.environ[var] = data

    #Setup Frame Range 
    start_frame = int(os.environ.get('G_START'))
    end_frame = int(os.environ.get('G_END'))
    
    cmds.playbackOptions(edit=True,animationStartTime = start_frame)
    cmds.playbackOptions(edit=True,animationEndTime = end_frame)
    
    cmds.playbackOptions(edit=True,minTine = start_frame)
    cmds.playbackOptions(edit=True,maxTime = end_frame)