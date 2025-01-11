from flask import Flask, jsonify, request
import requests
from datetime import datetime
from time import sleep

app = Flask(__name__)
OMDB_API_KEY="ce17ec69"

@app.route("/")
def index():
    return "<h1>Hello, world</h1>"

@app.route("/now")
def now():
    now = datetime.now()
    return jsonify({"date: " : str(now)}), 200

@app.route("/search")
def search():
    search = request.args.get('movie')
    res = requests.get(f"http://www.omdbapi.com/?s={search}&apikey={OMDB_API_KEY}")
    sleep(5)
    return jsonify(res.json()), 200

app.run(debug=True)