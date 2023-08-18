#save notes

import os
import json
import datetime


shot_dir = "D:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001"

def save_notes(shot_dir):

    shot_status = "bin/data/shot_status.json"
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

    #check last note match and update
    last_notes = os.listdir(os.path.join(shot_dir,"notes"))
    last_notes.sort()

    last_note_dir = os.path.join(shot_dir,"notes",last_notes[-1],filename)
    print(last_note_dir)
    load_note = open(last_note_dir,"r")
    last_note = load_note.read()
    load_note.close()
    print(last_note)

    #Save Notes
    cur_note = "Make it High res"

    

    if last_note is not cur_note:
   
        if not os.path.isdir(note_dir):
            os.makedirs(os.path.join(note_dir,"annotation"))
            note_file = os.path.join(note_dir,filename)

            for k,v in notes_data.items():
                if k == "Shot_AB001":
                    with open(note_file,"w") as n:
                        n.write(v)
    
    

save_notes(shot_dir)


# print(str(datetime.date.today()).replace("-","_"))
