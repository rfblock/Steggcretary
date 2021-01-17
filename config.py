import os

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SIGNING_SECRET = os.getenv('SIGNING_SECRET')
ACTIONS_JSON = os.getenv('ACTIONS_JSON')
BOT_UID = os.getenv('BOT_UID')

DEBUG = True