from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3

exercise_bp = Blueprint("exercise", __name__)

@exercise_bp.route("/", methods=["POST"])
@jwt_required()
def add_exercise():
    data = request.get_json()
    user_id = get_jwt_identity()["id"]
    activity = data["activity"]
    duration = data["duration"]
    date = data["date"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO exercise_logs (user_id, activity, duration, date) VALUES (?, ?, ?, ?)",
        (user_id, activity, duration, date),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Exercise log added successfully"}), 201

@exercise_bp.route("/", methods=["GET"])
@jwt_required()
def get_exercises():
    user_id = get_jwt_identity()["id"]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exercise_logs WHERE user_id = ?", (user_id,))
    logs = cursor.fetchall()
    conn.close()
    return jsonify({"logs": logs}), 200
