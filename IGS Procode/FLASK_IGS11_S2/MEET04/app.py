from flask import *
import mysql.connector
 
app = Flask(__name__)

mydb = mysql.connector.connect(
    host= "localhost",
    database = "ecommerce",
    user = "root",
    password = "root123"
)
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/simpan', methods=["POST", "GET"])
def simpan():
    cursor = mydb.cursor()
    nama = request.form["nama"]
    q = "INSERT INTO kota (nama) VALUES (%s)"
    data = (nama,)
    cursor.execute(q, data)
    mydb.commit()
    cursor.close()
    return redirect("data_view")

@app.route('/data_view')
def data_view():
    cursor = mydb.cursor()
    cursor.execute("select * from kota")
    data = cursor.fetchall()
    return render_template("data_view.html", data = data )

@app.route('/hapus/<id>')
def hapus(id):
    cursor = mydb.cursor()
    q = "delete from kota where id = %s"
    data = ( id, )
    cursor.execute( q, data )
    mydb.commit()
    cursor.close()
    return redirect("/data_view")

@app.route('/update/<id>')
def update(id):
    cursor = mydb.cursor()
    query = "select * from kota where id = %s"
    data = (id,)
    cursor.execute(query, data)
    value = cursor.fetchone()
    return render_template("data_update.html", value = value )

@app.route('/aksi_update', methods=["POST", "GET"])
def aksi_update():
    cursor = mydb.cursor()
    id = request.form["id"]
    nama = request.form["nama"]
    q = "UPDATE kota SET nama = %s WHERE id = %s"
    data = (nama, id)  # URUTAN DIUBAH
    cursor.execute(q, data)
    mydb.commit()
    cursor.close()
    return redirect("/data_view")


if __name__ == "__main__":
    app.run(debug=True)