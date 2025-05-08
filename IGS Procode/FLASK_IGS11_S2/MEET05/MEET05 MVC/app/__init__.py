from flask import Flask
from app.config import Config
from app.controllers.routes import routes_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    app.register_blueprint(routes_blueprint)
    
    return app