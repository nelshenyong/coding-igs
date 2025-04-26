from flask import Blueprint, render_template, request, redirect

from app.models.kota_model import kotaModel

routes_blueprint = Blueprint('routes', __name__)
@routes_blueprint.route('/')
@routes_blueprint.route('/home')
def home():
    return render_template("home.html")