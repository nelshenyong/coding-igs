from flask import Flask, render_template

app = Flask(__name__)

titleWeb= "MY PROJECT"

data = ["I", "G", "S"]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", titleWeb = titleWeb, data = data)
@app.route('/igs')
def igs():
    return render_template('igs.html', data = data)

if __name__  == '__main__':
    app.run(debug=True)
