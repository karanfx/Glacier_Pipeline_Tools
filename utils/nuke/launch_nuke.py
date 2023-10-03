# "nuke_path" "script/path.py"
# "nuke_path" -t "script/path.py"
def setup_env(toolname,proj,seq,shot,shot_dir,start_frame=1001,end_frame=1200):

    import os
    job = os.path.join(shot_dir,toolname)
    # os.environ['SHOT_DIR'] = 'shot_001/nuke'
    variables = {"SHOW" : str(proj), "SEQ": str(seq), "SHOT":str(shot),"SHOT_DIR": str(shot_dir),
                "JOB":str(job),"G_START": str(start_frame),"G_END": str(end_frame)}
     
    for var,val in variables:
        os.environ[var] = val


def launch_version(soft_dir,file_dir):
    import subprocess
    subprocess.Popen([soft_dir, file_dir])