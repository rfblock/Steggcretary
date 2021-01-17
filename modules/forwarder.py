import config
import requests
import json

def __get_replies(channel, ts):
    #(Parent thread) Get thread list, (Thread item) Get thread item
    return json.loads(requests.get('https://slack.com/api/conversations.replies', params={
            'channel': channel,
            'ts': ts
        }, headers={
            'Authorization': f'Bearer {config.SLACK_TOKEN}'
        }).content.decode('utf-8'))['messages']

def forwarder(data):
    reaction = data['event']['reaction']
    channel = data['event']['item']['channel']
    ts = data['event']['item']['ts']


    if data['event']['reaction'] == 'tallyho':
        replies = __get_replies(channel, ts)

        parent_ts = ts
        if 'thread_ts' in replies[0]:
            parent_ts = replies[0]['thread_ts']
            replies = __get_replies(channel, parent_ts)

        #If bot user found OR total messages ≥ 50
        if [x for x in replies if x['user'] == config.BOT_UID] or len(replies) >= 50:
            return '200'


        requests.post('https://slack.com/api/chat.postMessage', data={
            'channel': channel,
            'text': 'you called?',
            'thread_ts': parent_ts
        }, headers={
            'Authorization': f'Bearer {config.SLACK_TOKEN}'
        })
    return '200'