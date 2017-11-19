from flask import Blueprint
from utils import util_requests

frontend_bp = Blueprint('frontend', __name__, url_prefix='/frontend')


@frontend_bp.route('/')
def index():
	return 'Hello. Frontend is working!'


@frontend_bp.route('/mail')
def mail():
	endpoint = '/mail'

	data = {
	'to': 'joeffrey.gueroben'
	}

	result = util_requests.post_json_3pservice(endpoint, data)

	return result