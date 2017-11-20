import requests
import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename


backend_bp = Blueprint('backend', __name__, url_prefix='/backend')
FILE_LOCATION = '/home/joeffrey/code/github/playground/backend/upload'


@backend_bp.route('/')
def index():
	return 'Hello. Backend is working!'


@backend_bp.route('/mail', methods=['POST'])
def mail():
	try:
		print '--- req: ', requests
		to = request.json.get('to')
		print '---to: ', to

	except Exception as err:
		response_err = jsonify({'error': str(err)})
		response_err.status_code = 500
		return response_err

	return jsonify({"status": "success"})


@backend_bp.route('/savefile', methods=['POST'])
def save_file():
	try:
		print '--- backend: save_file()'
		if request.method == 'POST':
			if 'file' not in request.files:
				return jsonify({"status": "no file"})
			file = request.files['file']
			data = request.files['data']
			email__info = data.read()
			if file.filename == '':
				return jsonify({"status": "no file"})
			if file and data:
				filename = secure_filename(file.filename)
				file.save(os.path.join(FILE_LOCATION, filename))
	except Exception as err:
		print 'ERROR: ', str(err)
		return jsonify({"status": str(err)})
	return jsonify({"status": "success"})
