from flask import Flask
from app.config import Config
from app.controllers.routes import routes_blueprint
from app.controllers.routes_kategori import routes_kategori_blueprint
from app.controllers.routes_kategoripenjual import routes_kategoripenjual_blueprint
from app.controllers.routes_penjual import routes_penjual_blueprint
from app.controllers.routes_produk import routes_produk_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(routes_blueprint)
    app.register_blueprint(routes_kategori_blueprint)
    app.register_blueprint(routes_kategoripenjual_blueprint)
    app.register_blueprint(routes_penjual_blueprint)
    app.register_blueprint(routes_produk_blueprint)
    
    return app