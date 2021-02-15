from copy import deepcopy
import config
import json
from modules import actions
from modules.slack import chat, conversations, reactions
import random
import re
import time

rate_limits = {}

def check_rate_limit(channel, user):
	if user in actions.commands['users']:
		return actions.commands['users'][user]['rate_bypass']

	rates = actions.commands['rate_limit']
	limit = rates['*']['limit']
	if channel in rates:
		limit = rates[channel]['limit']
	elif channel.startswith('G'):
		limit = rates['G*']['limit']

	if limit < 0:
		return False

	if channel in rate_limits:
		last_ts = rate_limits[channel]['last_ts']
		delta_ts = time.time() - last_ts
		if delta_ts >= limit:
			return True
		return False
	else:
		rate_limits[channel] = {
			'last_ts': time.time()
		}
	return True


# "Call response" commands can be put inline
def parse_command(data):
	event = data['event']
	text = event['text']
	channel = event['channel']
	user = event['user']
	ts = event['ts']
	if not check_rate_limit(channel, user):
		chat.postEphemeral(channel=channel, text='Slow down! No one likes spam', user=user)
		return 'OK', 200
	print(text)
	print(user)
	commands = actions.commands['commands']
	base_pattern = actions.commands['base_regex'].format(config.BOT_UID, '{0}')

	# Grab the thread_ts from ts
	thread = conversations.replies(channel=channel, ts=ts)['messages'][0]
	thread_ts = ts
	if 'thread_ts' in thread:
		thread_ts = thread['thread_ts']

	if not actions.commands['thread']: thread_ts = None

	# Help Command
	if re.search(base_pattern.format('help'), text):
		_help = commands['help']
		blocks = [_help['header'], _help['divide']]
		for key in commands.keys():
			context = commands[key]['help']
			template = deepcopy(_help['template'])
			template['text']['text'] = template['text']['text'].format(context[0], context[1], context[2])
			template['accessory']['alt_text'] = context[3]
			template['accessory']['image_url'] = context[4]
			blocks.append(template)
			blocks.append(_help['divide'])
		blocks.append(_help['footer'])
		chat.postMessage(channel=channel, blocks=json.dumps(blocks), thread_ts=thread_ts)
		return 'OK', 200

	# Hello-Wave Command
	if re.search(commands['hello']['pattern'].format(config.BOT_UID), text):
		name = random.choice(commands['hello']['names'])
		reactions.add(channel=channel, name=name, timestamp=ts)
		return 'OK', 200

	for key in commands.keys():
		if 'message' in commands[key]:
			if re.search(base_pattern.format(key), text):
				chat.postMessage(channel=channel, blocks=json.dumps(commands[key]['message']), thread_ts=thread_ts)

	return 'OK', 200