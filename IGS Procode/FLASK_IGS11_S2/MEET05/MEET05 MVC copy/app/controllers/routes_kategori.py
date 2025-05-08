from flask import Blueprint, render_template, request, redirect, url_for
from app.models.kategori_model import kategoriModel

routes_kategori_blueprint = Blueprint('routes_kategori', __name__)

@routes_kategori_blueprint.route('/kategori')
def kategori():
    return render_template("kategori.html")

@routes_kategori_blueprint.route('/kategori_view')
def kategori_view():
    kategori = kategoriModel()
    data = kategori.get_all_kategori()
    return render_template("kategori_view.html", data=data)

@routes_kategori_blueprint.route('/simpan_kategori', methods=['POST'])
def simpan_kategori():
    nama = request.form['nama']
    kategori = kategoriModel()
    kategori.save_kategori(nama)
    return redirect(url_for('routes_kategori.kategori_view'))

@routes_kategori_blueprint.route('/update_kategori/<int:id>')
def update_kategori(id):
    kategori = kategoriModel()
    data = kategori.get_kategori_by_id(id)
    return render_template("kategori_update.html", value=data)

@routes_kategori_blueprint.route('/aksi_update_kategori', methods=['POST'])
def aksi_update_kategori():
    id = request.form['id']
    nama = request.form['nama']
    kategori = kategoriModel()
    kategori.update_kategori(id, nama)
    return redirect(url_for('routes_kategori.kategori_view'))

@routes_kategori_blueprint.route('/hapus_kategori/<int:id>')
def hapus_kategori(id):
    kategori = kategoriModel()
    kategori.delete_kategori(id)
    return redirect(url_for('routes_kategori.kategori_view')) 