from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from gsheet import sheet
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Player

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    try:
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
        logger.info(f"Successfully created player in database: {player.name}")

        # Try to add data to Google Sheets if available
        if sheet is not None:
            try:
                row = [
                    player.id,
                    player.name,
                    player.age,
                    player.games_played,
                    player.highest_score,
                    player.lowest_score,
                    player.current_score
                ]
                logger.info(f"Attempting to add row to Google Sheets: {row}")
                sheet.append_row(row)
                logger.info(f"Successfully added player {player.name} to Google Sheets")
            except Exception as e:
                logger.error(f"Failed to add player to Google Sheets: {str(e)}")
                # Continue even if Google Sheets update fails
                pass
        else:
            logger.error("Google Sheets connection is not available")

        return jsonify(player.to_dict()), 201
    except Exception as e:
        logger.error(f"Error creating player: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

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

@app.route("/")
def index():
    return "It Works"

if __name__ == "__main__":
    app.run(debug=True)
