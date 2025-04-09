from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    database="ecomerce",
    user="root",
    password="root123"
)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/simpan', methods=["POST"])
def simpan():
    if request.method == "POST":
        nama = request.form['nama']  # Ambil input dari form
        
        cursor = mydb.cursor()
        q = "INSERT INTO kota (nama) VALUES (%s)"  # Hanya masukkan 'nama'
        values = (nama,)
        cursor.execute(q, values)
        mydb.commit()
        cursor.close()
        
        return redirect(url_for("data_view"))  # Perbaikan redirect

@app.route('/data_view')
def data_view():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM kota")  # Ambil semua data dari kota
    data = cursor.fetchall()
    cursor.close()
    return render_template("data_view.html", data=data)

@app.route('/hapus/<int:id>')
def hapus(id):
    cursor = mydb.cursor()
    q = "DELETE FROM kota WHERE id=%s"
    cursor.execute(q, (id,))  # Perbaikan parameter query
    mydb.commit()
    cursor.close()
    
    return redirect(url_for("data_view"))  # Perbaikan redirect

if __name__ == "__main__":
    app.run(debug=True)