from flask import Blueprint, render_template, request, redirect, url_for
from app.models.kategoripenjual_model import kategoripenjualModel

routes_kategoripenjual_blueprint = Blueprint('routes_kategoripenjual', __name__)

@routes_kategoripenjual_blueprint.route('/kategoripenjual_view')
def kategoripenjual_view():
    model = kategoripenjualModel()
    data = model.get_all_kategoripenjual()
    return render_template('kategoripenjual_view.html', data=data)

@routes_kategoripenjual_blueprint.route('/kategoripenjual')
def kategoripenjual():
    model = kategoripenjualModel()
    penjual = model.get_all_penjual()
    kategori = model.get_all_kategori()
    return render_template('kategoripenjual.html', penjual=penjual, kategori=kategori)

@routes_kategoripenjual_blueprint.route('/simpan_kategoripenjual', methods=['POST'])
def simpan_kategoripenjual():
    penjualid = request.form['penjualid']
    kategoriid = request.form['kategoriid']
    model = kategoripenjualModel()
    model.save_kategoripenjual(penjualid, kategoriid)
    return redirect(url_for('routes_kategoripenjual.kategoripenjual_view'))

@routes_kategoripenjual_blueprint.route('/update_kategoripenjual/<int:id>')
def update_kategoripenjual(id):
    model = kategoripenjualModel()
    value = model.get_kategoripenjual_by_id(id)
    penjual = model.get_all_penjual()
    kategori = model.get_all_kategori()
    return render_template('kategoripenjual_update.html', value=value, penjual=penjual, kategori=kategori)

@routes_kategoripenjual_blueprint.route('/aksi_update_kategoripenjual', methods=['POST'])
def aksi_update_kategoripenjual():
    id = request.form['id']
    penjualid = request.form['penjualid']
    kategoriid = request.form['kategoriid']
    model = kategoripenjualModel()
    model.update_kategoripenjual(id, penjualid, kategoriid)
    return redirect(url_for('routes_kategoripenjual.kategoripenjual_view'))

@routes_kategoripenjual_blueprint.route('/hapus_kategoripenjual/<int:id>')
def hapus_kategoripenjual(id):
    model = kategoripenjualModel()
    model.delete_kategoripenjual(id)
    return redirect(url_for('routes_kategoripenjual.kategoripenjual_view')) 