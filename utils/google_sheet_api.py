import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import json
#Connect and get the Data from Google Sheets/Drive API
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("bin\creds\pipelineapi-393910-b7f6abbedec1-credential_key.json",scope)
client = gspread.authorize(creds)
sheet = client.open("Studio_Management").sheet1


col = sheet.col_values(5)

#Get Artist Data from Sheets
data =[]
for i,name in enumerate(col):
    i = i+1
    if name == "Karan":
        artist_data = sheet.row_values(i)
        # pprint(artist_data)
        data.append(artist_data)
print(data)


#Save Json File
with open("bin/data/shot_status.json", "w") as file:
    json.dump(data,file)     


# print(col)