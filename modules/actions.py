import config
import json
import os
with open(config.ACTIONS_PATH) as f:
	actions_json = json.load(f)

reminders = actions_json['reminders']
forwarder = actions_json['forwarder']
pfp = actions_json['pfp']
github = actions_json['github']
moderator = actions_json['moderator']