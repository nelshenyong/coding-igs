from flask import Blueprint, render_template, request, redirect, url_for
from app.models.penjual_model import penjualModel

routes_penjual_blueprint = Blueprint('routes_penjual', __name__)

@routes_penjual_blueprint.route('/penjual_view')
def penjual_view():
    model = penjualModel()
    data = model.get_all_penjual()
    return render_template('penjual_view.html', data=data)

@routes_penjual_blueprint.route('/penjual')
def penjual():
    model = penjualModel()
    kota = model.get_all_kota()
    return render_template('penjual.html', kota=kota)

@routes_penjual_blueprint.route('/simpan_penjual', methods=['POST'])
def simpan_penjual():
    nama = request.form['nama']
    alamat = request.form['alamat']
    kotaid = request.form['kotaid']
    model = penjualModel()
    model.save_penjual(nama, alamat, kotaid)
    return redirect(url_for('routes_penjual.penjual_view'))

@routes_penjual_blueprint.route('/update_penjual/<int:id>')
def update_penjual(id):
    model = penjualModel()
    value = model.get_penjual_by_id(id)
    kota = model.get_all_kota()
    return render_template('penjual_update.html', value=value, kota=kota)

@routes_penjual_blueprint.route('/aksi_update_penjual', methods=['POST'])
def aksi_update_penjual():
    id = request.form['id']
    nama = request.form['nama']
    alamat = request.form['alamat']
    kotaid = request.form['kotaid']
    model = penjualModel()
    model.update_penjual(id, nama, alamat, kotaid)
    return redirect(url_for('routes_penjual.penjual_view'))

@routes_penjual_blueprint.route('/hapus_penjual/<int:id>')
def hapus_penjual(id):
    model = penjualModel()
    model.delete_penjual(id)
    return redirect(url_for('routes_penjual.penjual_view')) 