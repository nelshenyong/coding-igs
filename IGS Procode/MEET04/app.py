from flask import *
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    database = "ecommerce",
    user = "root",
 password = ""
)   

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/data')
def data():
    return render_template("data.html")
    
@app.route('/simpan', methods = ["POST", "GET"])
def simpan():
    cursor = mydb.cursor()
    nama = request.form["nama"]
    q = "insert into kota (id, nama ) values( %s, %s )"
    data ( '', nama )
    cursor.execute( q, data )
    mydb.commit()
    cursor.close()
    return render_template("data_view.html")

@app.route('/data_view')
def data_view():
    cursor = mydb.cursor()
    cursor.execute("select * from kota")
    data = cursor.fetchall()
    return render_template("data_view.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)