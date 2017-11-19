from flask import Flask

app = Flask(__name__)

from services import backend
app.register_blueprint(backend.backend_bp)