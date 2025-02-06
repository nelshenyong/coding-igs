from flask import *
import secrets

app = Flask('__name__')
app.secret_key = secrets.token_hex(16)

dataUsers = [
    {
        'username': 'admin',
        'password': 'admin',
        'role': 'admin'
    },
    {
        'username': 'guest',
        'password': 'guest',
        'role': 'guest'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    if 'user' in session and session['user'] == dataUsers[0]['username']:
        return render_template('admin.html')
    else:
        return redirect(url_for('login'))

@app.route('/guest')
def guest():
    if 'user' in session and session['user'] == dataUsers[1]['username']:
        return render_template('guest.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        for user in dataUsers:
            if username == user['username'] and password == user['password']:
                session['user'] = username
                if user['role'] == 'admin':
                    return redirect(url_for('admin'))
                elif user['role'] == 'guest':
                    return redirect(url_for('guest'))
        
        return render_template('login.html', error="Invalid username or password")
    
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