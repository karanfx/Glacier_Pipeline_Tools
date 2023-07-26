import json

with open("bin\data\shot_status.json") as f:
            shots = json.load(f)


print(type(shots))