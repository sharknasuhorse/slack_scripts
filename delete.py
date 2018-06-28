import os
import json
import requests
from slackclient import SlackClient
delete_channels =["random"]

slack_token = os.environ["SLACK_API_TOKEN_LEGA"]
slack_api_token = "hogehoge"
sc = SlackClient(slack_token)
channel_list_res = sc.api_call("channels.list")
channel_list = channel_list_res["channels"]

for a in channel_list:
  for b in delete_channels:
    if a["name"] == b:
      ##delete対象チャンネル
      res = requests.get('https://slack.com/api/channels.history?token=' + slack_api_token + '&channel=' + a["id"] + '&count=' + '1000')
      channelMessages = json.loads(res.text)
      channelMessages = channelMessages["messages"]
      for c in channelMessages:
        try:
          if c["user"] == "UA9NX5L3H":
            sc.api_call("chat.delete",channel= a["id"],ts=c["ts"],)
        except:
          pass
exit()
