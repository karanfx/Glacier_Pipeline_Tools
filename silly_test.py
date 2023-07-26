import json

from utils.google_sheet_api import get_status

# get_status('Harish')

with open("bin\data\shot_status.json") as f:
            shots = json.load(f)

        # shots =  ["Show01", "Seq_AB", "Shot_AB001", "Fire", "Karan", "Ready to Start", "7/25/2023", "7/31/2023", "Fire on Jungle"]
for shot in shots:
    print(type(shot))
    print(shot)
    shot.pop(0)
    shot.remove('Rakesh')
    print(shot)