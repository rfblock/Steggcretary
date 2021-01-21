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
- SIGNING_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

## Features
Things `Steggcretary` can do right now:
- [X] Forward messages via :cc-steggy:
- [ ] Change PFP based on status
- [ ] Show github notifications
- [ ] Moderate channels
