# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://karanmirajkar.atlassian.net/rest/api/3/issue/GPT-3"

auth = HTTPBasicAuth("karan.fxartist@gmail.com", "ATATT3xFfGF0vSsZ4ILg-3TqJBrFwmq6CZVUAlDyelcehKo4dCkGo2x4pKMWtOwygHgedYH_XuFSbusDNcPkHUwNSlESuS6ce9bqXx6aJOdUyJI2PdxSFjBJfIpvSE65TRb3tHxhItseZ5DH8oT8rZnD0nLLFNl0z3rXVtFbyfKYQqZzrm6AyTQ=4C10CEF5")

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