import requests
from flask import Flask, request, abort
import schedule
import hmac
import hashlib
import config
from modules import commands, forwarder, github
from modules.slack import chat

app = Flask(__name__)
app.config.from_object('config')

@app.route('/slack/events', methods=['POST'])
def events_api():
	# URL Verification for Events API
	request_data = request.get_json()
	if request_data['type'] == 'url_verification':
		return request_data
	return {
		'reaction_added': forwarder.forwarder,
		'app_mention': commands.parse_command
	}[request_data['event']['type']](request_data)

@app.route('/github/events', methods=['POST'])
def github_api():

	signature = request.headers.get('X-Hub-Signature')
	if not signature or not signature.startswith('sha1='):
		abort(400, 'X-Hub-Signature required')
	
	digest = hmac.new(config.GITHUB_WEBHOOK_SECRET.encode(), request.data, hashlib.sha1).hexdigest()

	if not hmac.compare_digest(signature, 'sha1=' + digest):
		abort(400, 'Invalid signature')
	
	request_data = request.get_json()
	github.github_notif(request_data)

	return 'OK', 200

	#TODO: ADD Reminders
	#TODO: ADD PFP changer
	#TODO: ADD moderation
	#TODO: 1/100 chance of steggcrataty

if __name__ == '__main__':
	app.run(port=8080)
