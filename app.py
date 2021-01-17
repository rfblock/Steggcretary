import requests
from flask import Flask, request
import schedule
from modules import forwarder

app = Flask(__name__)
app.config.from_object('config')

@app.route('/slack/events', methods=['POST'])
def events_api():
	### URL Verification for Events API ###
	if request.json['type'] == 'url_verification':
		return request.json

	#TODO: ADD Reminders
	#TODO: ADD PFP changer
	#TODO: ADD github notifs
	#TODO: ADD moderation
	return {
		'reaction_added': forwarder.forwarder
	}[request.json['event']['type']](request.json)

if __name__ == '__main__':
	app.run(port=8080)
