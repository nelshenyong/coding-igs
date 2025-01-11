from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    web_title = "Halaman utama"
    return render_template('home.html', web_title=web_title)
        

@app.route("/about")
def about():
    web_title = "Halaman kedua"
    return render_template('about.html', web_title=web_title)

@app.route("/usia", methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = 2024
        usia = tahun_sekarang - tahun_lahir
        return render_template('usia.html', usia=usia)
    return render_template('usia.html', usia=None)