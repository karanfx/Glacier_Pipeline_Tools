import json
import os

studiodir = "D:/Work/houdinifx/pipe_test/"
username = 'Karan'

# from google_sheet_api import get_status

def create_shot_dirs(studiodir):
    with open("bin\data\shot_status.json") as f:
        data = json.load(f)

    # shots = shots[1:]
    show_idx = data[0].index('Show')
    seq_idx = data[0].index('Sequence')
    shot_idx = data[0].index('Shot')
    # print(show_idx,seq_idx,shot_idx)

    data.pop(0)
    for task in data:
        
        show_name = task[show_idx]
        seq_name = task[seq_idx]
        shot_name = task[shot_idx]
        # print(show_name,seq_name,shot_name)
        shotdir = os.path.join(studiodir,show_name,seq_name,shot_name)
        print(shotdir)
        

        with open("bin/data/folder_struct.json") as f:
            dirs = json.load(f)

        for k,v in dirs.items():
            for dir in v:
                path = os.path.join(shotdir,k,dir)
                if not os.path.isdir(path):
                    os.makedirs(path)
                print(path)


create_shot_dirs(studiodir)