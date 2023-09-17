# "nuke_path" "script/path.py"
# "nuke_path" -t "script/path.py"

def launch_version(soft_dir,file_dir):
    import subprocess
    subprocess.Popen([soft_dir, file_dir])