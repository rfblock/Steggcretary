import os
from dotenv import load_dotenv
load_dotenv()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
ACTIONS_PATH = os.getenv('ACTIONS_PATH')
BOT_UID = os.getenv('BOT_UID')
GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")

DEBUG = True