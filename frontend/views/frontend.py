from flask import Blueprint, jsonify
from utils import util_requests
import requests
import json


frontend_bp = Blueprint('frontend', __name__, url_prefix='/frontend')


@frontend_bp.route('/')
def index():
	return 'Hello. Frontend is working!'


@frontend_bp.route('/mail')
def mail():
	endpoint = '/mail'
	data = {
	'to': 'foo.bar'
	}
	result = util_requests.post_json_3pservice(endpoint, data)
	return result


@frontend_bp.route('/upload')
def upload():
	endpoint = 'http://localhost:7001/backend/savefile'
	email = {
	'to': 'foo.bar@gmail.com',
	'subject': 'Test Email',
	'body': 'This is the body.',	
	}
	#file = open('Python Tricks.pdf', 'rb')
	file = ('Python Tricks2.pdf', open('Python Tricks.pdf', 'rb'), 'application/octet-stream')
	data = ('Email', json.dumps(email), 'application/json')
	files = {
		'file': file,
		'data': data,
		}
	r = requests.post(endpoint, files=files)
	return r.text
