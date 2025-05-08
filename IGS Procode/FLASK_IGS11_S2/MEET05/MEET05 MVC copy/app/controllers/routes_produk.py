from flask import Blueprint, render_template, request, redirect, url_for
from app.models.produk_model import produkModel

routes_produk_blueprint = Blueprint('routes_produk', __name__)

@routes_produk_blueprint.route('/produk_view')
def produk_view():
    model = produkModel()
    data = model.get_all_produk()
    return render_template('produk_view.html', data=data)

@routes_produk_blueprint.route('/produk')
def produk():
    model = produkModel()
    penjual = model.get_all_penjual()
    return render_template('produk.html', penjual=penjual)

@routes_produk_blueprint.route('/simpan_produk', methods=['POST'])
def simpan_produk():
    nama = request.form['nama']
    harga = request.form['harga']
    penjualid = request.form['penjualid']
    model = produkModel()
    model.save_produk(nama, harga, penjualid)
    return redirect(url_for('routes_produk.produk_view'))

@routes_produk_blueprint.route('/update_produk/<int:id>')
def update_produk(id):
    model = produkModel()
    value = model.get_produk_by_id(id)
    penjual = model.get_all_penjual()
    return render_template('produk_update.html', value=value, penjual=penjual)

@routes_produk_blueprint.route('/aksi_update_produk', methods=['POST'])
def aksi_update_produk():
    id = request.form['id']
    nama = request.form['nama']
    harga = request.form['harga']
    penjualid = request.form['penjualid']
    model = produkModel()
    model.update_produk(id, nama, harga, penjualid)
    return redirect(url_for('routes_produk.produk_view'))

@routes_produk_blueprint.route('/hapus_produk/<int:id>')
def hapus_produk(id):
    model = produkModel()
    model.delete_produk(id)
    return redirect(url_for('routes_produk.produk_view')) 