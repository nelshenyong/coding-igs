from flask import Flask, render_template, request, redirect, url_for, session
import secrets
from datetime import timedelta

app = Flask(__name__)  # Perbaikan nama
app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=5)

users = [
    {"username": "admin", "password": "1234", "role": "admin"},
    {"username": "guest", "password": "4321", "role": "anggota"},
    {"username": "ketua", "password": "123", "role": "ketua"},
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    if "user" in session and session["role"] == "admin":
        return render_template("admin.html")
    return redirect(url_for("login"))

@app.route("/guest")
def guest():
    if "user" in session and session["role"] == "anggota":
        return render_template("guest.html")
    return redirect(url_for("login"))

@app.route("/ketua")
def ketua():
    if "user" in session and session["role"] == "ketua":
        return render_template("ketua.html")
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for user in users:
            if username == user["username"] and password == user["password"]:
                session["user"] = username
                session["role"] = user["role"]
                if user["role"] == "admin":
                    return redirect(url_for("admin"))
                elif user["role"] == "anggota":
                    return redirect(url_for("guest"))
                elif user["role"] == "ketua":
                    return redirect(url_for("ketua"))
        return render_template("login.html", error="Username atau password salah!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/bio", methods=["POST", "GET"])
def bio():
    if request.method == "POST":
        return render_template(
            "bio.html",
            nama=request.form.get("nama"),
            kelas=request.form.get("kelas"),
            email=request.form.get("email"),
            tempat=request.form.get("tempat"),
            tgl=request.form.get("tgl"),
            cita=request.form.get("cita"),
            agama=request.form.get("agama"),
            tentang=request.form.get("tentang"),
        )
    return render_template("bio.html")

if __name__ == "__main__":  # Perbaikan nama
    app.run(debug=True)
