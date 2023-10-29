# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

api_cred = "E:/Work/python_dev/Glacier_pipeline_tools/creds/jira_api_cred.json"


#get email and password
import json
with open(api_cred) as config_file:
    config = json.load(config_file)

MAIL_ID = config.get("MAIL_ID")
API_KEY = config.get("API_KEY")
    

url = "https://karanmirajkar.atlassian.net/rest/api/3/issue/GPT-3"

auth = HTTPBasicAuth(MAIL_ID, API_KEY)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
issue_json = json.loads(response.text)
# issue_json.get("summary")
# issue_json["summary"]
import pprint
pprint.pprint(issue_json.get("fields").get("summary"))
# print(json.dumps(issue_json, sort_keys=True, indent=4, separators=(",", ": ")))