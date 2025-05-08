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
@app.route('/')
def index():
    siswa_list = Siswa.query.all()
    return render_template('index.html', siswa_list=siswa_list)

if __name__ == '__main__':
    app.run(debug=True)