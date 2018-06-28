import json
import requests


slack_api_token = ""

res = requests.get("https://slack.com/api/files.list?token=" + slack_api_token)
files_list = json.loads(res.text)
files_list = files_list["files"]

for file in files_list:
  if file["user"] == "UA9NX5L3H":
    print(file["id"])
    res = requests.get("https://slack.com/api/files.delete?token=" + slack_api_token + "&file=" + file["id"])
  else:
    pass
