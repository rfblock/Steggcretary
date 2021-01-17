import config
import requests
import json
import random
from modules import actions
from modules.slack import chat, conversations
def __get_replies(channel, ts):
    return conversations.replies(channel=channel, ts=ts)['messages']

def forwarder(data):
    user = data['event']['user']
    reaction = data['event']['reaction']
    channel = data['event']['item']['channel']
    ts = data['event']['item']['ts']

    if reaction == actions.forwarder['trigger']:
        replies = __get_replies(channel, ts)

        #If thread item, get parent thread
        #When you request the ts of a thread item, slack only returns the single message, so you have to do this horribleness
        parent_ts = ts
        if 'thread_ts' in replies[0]:
            parent_ts = replies[0]['thread_ts']
            replies = __get_replies(channel, parent_ts)

        #If bot user found OR total messages ≥ 50
        if [x for x in replies if x['user'] == config.BOT_UID] or len(replies) >= 50:
            return '200'

        message = random.choice(actions.forwarder['messages']).format(f'<@{user}>')

        chat.postMessage(channel=channel, text=message, thread_ts=parent_ts)
    return '200'