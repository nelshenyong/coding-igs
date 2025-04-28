from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Player

@app.route("/players", methods=["GET"])
def get_players():
    players = Player.query.all()
    return jsonify([p.to_dict() for p in players]), 200

@app.route("/players/<int:player_id>", methods=["GET"])
def get_player(player_id):
    player = Player.query.get(player_id)
    if player:
        return jsonify(player.to_dict()), 200
    return jsonify({"status": "not found"}), 404

@app.route("/players", methods=["POST"])
def create_player():
    data = request.json
    required_fields = ["name", "age"]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    
    player = Player(
        name=data["name"],
        age=int(data["age"]),
        games_played=int(data.get("games_played", 0)),
        highest_score=int(data.get("highest_score", 0)),
        lowest_score=int(data.get("lowest_score", 0)),
        current_score=int(data.get("current_score", 0))
    )
    db.session.add(player)
    db.session.commit()
    return jsonify(player.to_dict()), 201

@app.route("/players/<int:player_id>", methods=["PATCH"])
def update_player(player_id):
    player = Player.query.get(player_id)
    if player:
        data = request.json
        valid_fields = ["name", "age", "games_played", "highest_score", "lowest_score", "current_score"]
        
        for field in valid_fields:
            if field in data:
                setattr(player, field, data[field])
        
        db.session.commit()
        return jsonify(player.to_dict()), 200

    return jsonify({"status": "not found"}), 404

@app.route("/players/<int:player_id>", methods=["DELETE"])
def delete_player(player_id):
    player = Player.query.get(player_id)
    if player:
        db.session.delete(player)
        db.session.commit()
        return jsonify({"message": "Player deleted"}), 200
    return jsonify({"status": "not found"}), 404


data = {
    "kevin": {
        "Name": "Kevin",
        "Class": "11 IPA KOMPUTER 1",
        "Hobbies": ["Bulu Tangkis", "Futsal", "Billiard"],
        "Age": 20
    },
}

@app.route("/")
def index():
    return "It Works"

@app.route("/me")
def me():
    return render_template("Me.html")

@app.route("/student/<string:name>")
def student(name):
    student_data = data.get(name.lower())
    if student_data:
        return jsonify(student_data), 200
    return jsonify({"status": "not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
