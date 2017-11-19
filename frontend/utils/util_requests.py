import requests
from flask import jsonify


backend_url = 'http://localhost:7001/backend'


def post_json_3pservice(endpoint, data):
	url = backend_url + endpoint
	result = requests.post(url, json=data)
	result_json = result.json()
	return jsonify(result_json)