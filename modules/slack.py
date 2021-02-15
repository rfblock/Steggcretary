import config
import requests
import json

class __chat:
	""""""
	def __init__(self):
		pass

	def delete(self, token=config.SLACK_TOKEN, channel=None, ts=None, as_user=None):
		"""Sends POST request to chat.delete, returns dict. See https://api.slack.com/methods/chat.delete for more"""
		return json.loads(requests.post('https://slack.com/api/chat.delete', data={
			'channel': channel,
			'ts': ts,
			'as_user': as_user
		}, headers={
			'Authorization': f'Bearer {token}'
		}).content.decode('utf-8'))

	def postEphemeral(self, token=config.SLACK_TOKEN, attachments=None, channel=None, text=None, user=None, as_user=None, blocks=None, icon_emoji=None, icon_url=None, link_names=None, parse=None, thread_ts=None, username=None):
		"""Sends POST request to chat.postEphemeral, returns dict. See https://api.slack.com/methods/chat.postEphemeral for more"""
		return json.loads(requests.post('https://slack.com/api/chat.postEphemeral', data={
			'attachments': attachments,
			'channel': channel,
			'text': text,
			'user': user,
			'as_user': as_user,
			'blocks': blocks,
			'icon_emoji': icon_emoji,
			'icon_url': icon_url,
			'link_names': link_names,
			'parse': parse,
			'thread_ts': thread_ts,
			'username': username
		}, headers={
			'Authorization': f'Bearer {token}'
		}).content.decode('utf-8'))

	def postMessage(self, token=config.SLACK_TOKEN, channel=None, text=None, as_user=None, attachments=None, blocks=None, icon_emoji=None, icon_url=None, mrkdwn=None, parse=None, reply_broadcast=None, thread_ts=None, unfurl_links=None, unfurl_media=None, username=None):
		"""Sends POST request to chat.postMessage, returns dict. See https://api.slack.com/methods/chat.postMessage for more"""
		return json.loads(requests.post('https://slack.com/api/chat.postMessage', data={
			'channel': channel,
			'text': text,
			'as_user': as_user,
			'attachments': attachments,
			'blocks': blocks,
			'icon_emoji': icon_emoji,
			'icon_url': icon_url,
			'mrkdwn': mrkdwn,
			'parse': parse,
			'reply_broadcast': reply_broadcast,
			'thread_ts': thread_ts,
			'unfurl_links': unfurl_links,
			'unfurl_media': unfurl_media,
			'username': username
		}, headers={
			'Authorization': f'Bearer {token}'
		}).content.decode('utf-8'))
chat = __chat()

class __conversations:
	def __init__(self):
		pass
	
	#NOTE: Cannot use application/json yet, must use application/x-www-form-urlencoded
	def replies(self, token=config.SLACK_TOKEN, channel=None, ts=None, cursor=None, inclusive=None, latest=None, limit=None, oldest=None):
		"""Sends GET request to conversations.replies, returns dict. See https://api.slack.com/methods/conversations.replies for more"""
		return json.loads(requests.get('https://slack.com/api/conversations.replies', params={
			'channel': channel,
			'ts': ts,
			'cursor': cursor,
			'inclusive': inclusive,
			'latest': latest,
			'limit': limit,
			'oldest': oldest
		}, headers={
			'Authorization': f'Bearer {token}'
		}).content.decode('utf-8'))
conversations = __conversations()

class __reactions:
	def __init__(self):
		pass
	
	def add(self, token=config.SLACK_TOKEN, channel=None, name=None, timestamp=None):
		"""Sends POST request to reactions.add, returns dict. See https://api.slack.com/methods/reactions.adds for more"""
		return json.loads(requests.post('https://slack.com/api/reactions.add', data={
			'token': token,
			'channel': channel,
			'name': name,
			'timestamp': timestamp
		}, headers={
			'Authorization': f'Bearer {token}'
		}).content.decode('utf-8'))
reactions = __reactions()