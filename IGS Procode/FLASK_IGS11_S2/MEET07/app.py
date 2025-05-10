from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kelas = db.Column(db.String(100), nullable=False)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    
def cekuser():
    if not User.query.first(): # sama aja dengan -> if len(User.query.all())
        newuser = User(username = "admin")
        newuser.password = generate_password_hash("qwerty")
        db.session.add(newuser)
        db.session.commit()
    pass
    

@app.route('/', methods = ["POST", "GET"])
def index():
    if 'username' in session:
        if request.method == "POST":
            siswa = Siswa( nama = request.form["nama"], kelas = request.form["kelas"])
            db.session.add(siswa)
            db.session.commit()
            return redirect("/")
        siswa_list = Siswa.query.all()
        return render_template('index.html', siswa_list=siswa_list)
    return render_template("login.html")
        

# @app.route('/simpan', methods=["POST","GET"])
# def simpan():
#     siswa = Siswa( nama = request.form["nama"], kelas = request.form["kelas"])
#     db.session.add(siswa)
#     db.session.commit()
#     return redirect("/")

@app.route('/hapus/<id>')
def hapus(id):
    siswa = Siswa.query.get(id)
    db.session.delete(siswa)
    db.session.commit()
    return redirect("/")

@app.route('/update/<id>', methods=["POST","GET"])
def update(id):
    siswa = Siswa.query.get(id)
    if request.method == "POST":
        siswa.nama = request.form["nama"]
        siswa.kelas = request.form["kelas"]
        db.session.commit()
        return redirect("/")
    return render_template("update.html", siswa = siswa)

# @app.route('/update/<id>')
# def update(id):
#     siswa = Siswa.query.get(id)
#     return render_template("update.html", siswa = siswa)

# @app.route('/aksi_update', methods=["POST","GET"])
# def aksi_update():
#     siswa = Siswa.query.get( request.form["id"] )
#     siswa.nama = request.form["nama"]
#     siswa.kelas = request.form["kelas"]
#     db.session.commit()
#     return redirect("/")

@app.route('/login', methods = ["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username = username).first()
    if user and check_password_hash(user.password, password):
        session['username'] = username 
        return redirect("/")
    return redirect("/")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)