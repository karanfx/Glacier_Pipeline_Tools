import json
import os

shotdir = "D:\Work\houdinifx\pipe_test\shot_003"
def makesub_dirs(shotdir):
    with open("bin/data/folder_struct.json") as f:
        dirs = json.load(f)

    for k,v in dirs.items():
        for dir in v:
            path = os.path.join(shotdir,k,dir)
            os.makedirs(path)
            print(path)

# makesub_dirs(shotdir)
