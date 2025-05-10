from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kelas = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        siswa = Siswa(nama=request.form['nama'], kelas=request.form['kelas'])
        db.session.add(siswa)
        db.session.commit()
        return redirect('/')
    
    siswa_list = Siswa.query.all()
    return render_template('index.html', siswa_list=siswa_list)

@app.route('/hapus/<int:id>')
def hapus(id):
    siswa = Siswa.query.get(id)
    db.session.delete(siswa)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>')
def update(id):
    siswa = Siswa.query.get(id)
    return render_template('update.html', siswa=siswa)

@app.route('/aksi_update', methods=['POST', 'GET'])
def aksi_update():
    siswa = Siswa.query.get(request.form['id'])
    siswa.nama = request.form['nama']
    siswa.kelas = request.form['kelas']
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)