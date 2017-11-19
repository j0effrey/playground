from flask import Blueprint, request, jsonify


backend_bp = Blueprint('backend', __name__, url_prefix='/backend')


@backend_bp.route('/')
def index():
	return 'Hello. Backend is working!'


@backend_bp.route('/mail', methods=['POST'])
def mail():
	try:
		to = request.json.get('to')
		print '---to: ', to

	except Exception as err:
		response_err = jsonify({'error': str(err)})
		response_err.status_code = 500
		return response_err

	return jsonify({"status": "success"})
