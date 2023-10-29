import json
import os

#Import userID and tool dirs
user_json_path = "bin/data/user.json"
with open(user_json_path,"r") as uf:
    user_json = json.load(uf)
userdata = user_json.get('User_Data')

username = userdata.get('user')
studio_dir = userdata.get('studiodir')

tooldata = user_json.get('tools')
# print(tooldata)

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
        shotdir = os.path.join(studiodir,show_name,seq_name,shot_name,username)
        # print(shotdir)
        

        with open("bin/data/folder_struct.json") as f:
            dirs = json.load(f)

        for k,v in dirs.items():
            for dir in v:
                path = os.path.join(shotdir,k,dir)
                if not os.path.isdir(path):
                    os.makedirs(path)
                # print(path)

def create_libs(studiodir):
    libs = "libs"
   
    #show libs 
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
        
        
        #show Libs
        show_lib = os.path.join(studiodir,show_name,libs)
        if not os.path.isdir(show_lib):
            os.mkdir(show_lib)

        #seq libs
        seq_lib = os.path.join(studiodir,show_name,seq_name,libs)
        if not os.path.isdir(seq_lib):
            os.mkdir(seq_lib)

        #shot libs
        shot_lib = os.path.join(studiodir,show_name,seq_name,shot_name,libs)
        if not os.path.isdir(shot_lib):
            os.mkdir(shot_lib)
 

# print(studio_dir)
# print(username)
# create_libs(studio_dir)
# create_shot_dirs(studio_dir)