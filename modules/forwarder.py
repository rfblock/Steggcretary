import config
import requests
import json

def forwarder(data):
    reaction = data['event']['reaction']
    channel = data['event']['item']['channel']
    ts = data['event']['item']['ts']

    print(ts)

    if data['event']['reaction'] == 'tallyho':
        replies = json.loads(requests.get('https://slack.com/api/conversations.replies', params={
            'channel': channel,
            'ts': ts
        }, headers={
            'Authorization': f'Bearer {config.SLACK_TOKEN}'
        }).content.decode('utf-8'))['messages']

        #TODO: Change to config instead of magic ID
        #If bot user found OR total messages ≥ 50
        if [x for x in replies if x['user'] == 'U01K3418E4R'] or len(replies) >= 50:
            return '200'

        parent_ts = ts
        if 'thread_ts' in replies[0]:
            parent_ts = replies[0]['thread_ts']

        requests.post('https://slack.com/api/chat.postMessage', data={
            'channel': 'stegg',
            'text': 'you called?',
            'thread_ts': parent_ts
        }, headers={
            'Authorization': f'Bearer {config.SLACK_TOKEN}'
        })
    return '200'