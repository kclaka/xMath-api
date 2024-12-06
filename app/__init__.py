from routes.router import register_routes
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app)  # Allow all origins by default

    register_routes(app)
    return app