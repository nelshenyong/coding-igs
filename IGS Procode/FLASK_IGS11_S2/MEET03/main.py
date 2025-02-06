from flask import *
import secrets

app = Flask('__name__')
app.secret_key = secrets.token_hex(16)

dataUsers = [
    {
        'username': 'admin',
        'password': 'admin',
        'role': 'admin'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    if session.get('user'):
        return render_template('admin.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == dataUsers[0]["username"] and password == dataUsers[0]["password"]:
            session['user'] = username
            return redirect(url_for('admin'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/bio', methods=['GET', 'POST'])
def bio():
    return render_template('bio.html',
                           nama=request.form['nama'],
                           kelas=request.form['kelas'],
                           email=request.form['email'],
                           tempat=request.form['tempat'],
                           tgl=request.form['tgl'],
                           cita=request.form['cita'],
                           agama=request.form['agama'],
                           tentang=request.form['tentang']
                           )

if __name__ == '__main__':
    app.run(debug=True)