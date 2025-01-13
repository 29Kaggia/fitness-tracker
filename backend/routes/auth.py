from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
import sqlite3
import bcrypt

auth_bp = Blueprint("auth", __name__)

# Route for user registration
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Hash password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        # Insert new user into the database
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User already exists"}), 400
    finally:
        conn.close()

# Route for user login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user[3]):
        # Generate JWT token upon successful login
        token = create_access_token(identity={"id": user[0], "username": user[1]})
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Route for getting user profile
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()  # Protect route with JWT
def get_profile():
    # Get user ID from JWT token
    user_id = get_jwt_identity()["id"]
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"id": user[0], "username": user[1], "email": user[2]}), 200
    return jsonify({"error": "User not found"}), 404
