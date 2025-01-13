from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3

diet_bp = Blueprint("diet", __name__)

@diet_bp.route("/", methods=["POST"])
@jwt_required()
def add_diet():
    data = request.get_json()
    user_id = get_jwt_identity()["id"]
    food_item = data["food_item"]
    calories = data["calories"]
    date = data["date"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO diet_logs (user_id, food_item, calories, date) VALUES (?, ?, ?, ?)",
        (user_id, food_item, calories, date),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Diet log added successfully"}), 201

@diet_bp.route("/", methods=["GET"])
@jwt_required()
def get_diet_logs():
    user_id = get_jwt_identity()["id"]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diet_logs WHERE user_id = ?", (user_id,))
    logs = cursor.fetchall()
    conn.close()
    return jsonify({"logs": logs}), 200
