import config
import json
from modules import actions
from modules.slack import chat

def github_notif(data):
	#0 - user/repo
	#1 - compare url
	#2 - master url
	#3 - color
	#4 - user
	#5 - user link
	#6 - user icon
	#7 - commit url
	#8 - commit title
	#9 - repo link
	message = {
		'text': '', 
		'attachments': [{
			'fallback': '[{user_repo}] <{compare_url}|1 commit> pushed to <{master_url}|`master`>', 
			'color': '{color}', 
			'author_name': '{user}', 
			'author_link': '{user_link}', 
			'author_icon': '{user_icon}', 
			'text': '*<{compare_url}|1 commit> pushed to <{master_url}|`master`>*\n<{commit_url}|`abcdef12`> - {commit_title}', 
			'footer': '<{repo_link}|{user_repo}>', 
			'footer_icon': 'https://github.githubassets.com/favicon.ico'
		}]
	}
	if 'pull_request' in data:
		#handle pull request
		#(re)opened, edited, closed unmerged, closed merged
		action = data['action']
		pull_request = data['pull_request']
		repository = data['repository']
		user = pull_request['user']
		if action == 'opened':
			user_repo = repository['full_name']
			master_url = repository['html_url']

			pull_url = pull_request['html_url']
			pull_title = pull_request['title']

			username = user['login']
			user_link = user['html_url']
			user_icon = user['avatar_url']

			head_ref = pull_request['head']['ref']
			base_ref = pull_request['base']['ref']

			color = actions.github['deployed']
			message = {
				'text': '',
				'attachments': [{
					'fallback': f'[{user_repo}] New pull request <{pull_url}|`{head_ref}`> to <{pull_url}|`{base_ref}`>',
					'color': f'{color}',
					'author_name': f'{username}',
					'author_link': f'{user_link}',
					'author_icon': f'{user_icon}',
					'text': f'*New pull request <{pull_url}|`{head_ref}`> to <{pull_url}|`{base_ref}`>*\n<{pull_url}|`{head_ref}`> - {pull_title}',
					'footer': f'<{master_url}|{user_repo}>',
					'footer_icon': 'https://github.githubassets.com/favicon.ico'
				}]
			}
		#TODO: Edit
		#TODO: Closed
		#TODO: Merged
	elif 'issue' in data:
		#handle issue
		#opened, edited, deleted, closed
		pass
	elif 'commits' in data:
		#handle commits
		#push
		pass
	chat.postMessage(channel=actions.github['channel'], text=' ', attachments=json.dumps(message['attachments']))