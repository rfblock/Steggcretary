# Steggcretary
Steggcretary is a bot created for Steggy to manage his personal slack channels

## Developing

You can develop this in a Python venv. Simply run
```bash
source bin/activate
pip3 install -r requirements.txt
```

The slack events endpoint defaults to https://localhost:8080/slack/events
It needs the following environment variables
- SLACK_TOKEN=xxxx-your-token-here
- SIGNING_SECRET=0123456789abcdef0123456789abcdef
- ACTIONS_PATH=actions.json
- BOT_UID=U01K3418E4R

## Features
Things `Steggcretary` can do right now:
- [X] Forward messages via :cc-steggy:
- [ ] Change PFP based on status
- [ ] Show github notifications
- [ ] Moderate channels

