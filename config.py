import os
from dotenv import load_dotenv
load_dotenv()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SIGNING_SECRET = os.getenv('SIGNING_SECRET')
ACTIONS_PATH = os.getenv('ACTIONS_PATH')
BOT_UID = os.getenv('BOT_UID')

DEBUG = True