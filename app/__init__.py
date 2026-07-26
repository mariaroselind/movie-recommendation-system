from flask import Flask
from config import Config

def create_app():
    """Application Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # We import routes here to avoid circular dependencies
    with app.app_context():
        from . import routes

    return app