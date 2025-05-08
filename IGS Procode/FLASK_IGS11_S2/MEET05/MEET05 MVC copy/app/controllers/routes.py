from flask import Blueprint, render_template, request, redirect, url_for
from app.models.kota_model import kotaModel

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
@routes_blueprint.route('/home')
def home():
    return render_template("home.html")

@routes_blueprint.route('/data')
def data():
    return render_template("data.html")

@routes_blueprint.route('/data_view')
def data_view():
    kota = kotaModel()
    data = kota.get_all_kota()
    return render_template("data_view.html", data=data)

@routes_blueprint.route('/simpan', methods=['POST'])
def simpan():
    nama = request.form['nama']
    kota = kotaModel()
    kota.save_kota(nama)
    return redirect(url_for('routes.data_view'))

@routes_blueprint.route('/update/<int:id>')
def update(id):
    kota = kotaModel()
    data = kota.get_kota_by_id(id)
    return render_template("data_update.html", value=data)

@routes_blueprint.route('/aksi_update', methods=['POST'])
def aksi_update():
    id = request.form['id']
    nama = request.form['nama']
    kota = kotaModel()
    kota.update_kota(id, nama)
    return redirect(url_for('routes.data_view'))

@routes_blueprint.route('/hapus/<int:id>')
def hapus(id):
    kota = kotaModel()
    kota.delete_kota(id)
    return redirect(url_for('routes.data_view'))
