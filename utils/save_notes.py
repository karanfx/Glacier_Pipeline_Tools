#save notes

import os
import json
import datetime

shot_status = "bin/data/shot_status.json"
shot_dir = "D:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001"

def save_notes(shot_dir):

    with open(shot_status,"r") as f:
        data = json.load(f)
        # print(data)

    #Get Index 
    shot_index = data[0].index("Shot")
    notes_index = data[0].index("Notes")

    shot = data[1][shot_index]
    print(shot)

    data.pop(0)
    notes_data = {}
    for task in data:
        note = task[notes_index]
        shot = task[shot_index]
        notes_data.update({shot:note})

    #Create note version folders
    cur_date = str(datetime.date.today()).replace("-","_")
    filename = "notes.txt"
    note_dir = os.path.join(shot_dir,"notes",cur_date)
    
    if not note_dir:
        os.makedirs(os.path.join(note_dir,"annotation"))
    note_file = os.path.join(note_dir,filename)
    
    #Save Notes
    for k,v in notes_data.items():
        if k == "Shot_AB001":

            with open(note_file,"w") as n:
                n.write(v)

save_notes(shot_dir)


# print(str(datetime.date.today()).replace("-","_"))
