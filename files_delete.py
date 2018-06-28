"""This is a test program."""
import json
import requests


SLACK_API_TOKEN = ""

res = requests.get("https://slack.com/api/files.list?token=" + SLACK_API_TOKEN)
files_list = json.loads(res.text)
files_list = files_list["files"]

for file in files_list:
    if file["user"] == "UA9NX5L3H":
        print(file["id"])
        res = requests.get("https://slack.com/api/files.delete?token=" + SLACK_API_TOKEN + "&file=" + file["id"])
    else:
        pass
