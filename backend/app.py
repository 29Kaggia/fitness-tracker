from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from utils.db import init_db
from models import db
from routes.auth import auth_bp
from routes.exercise import exercise_bp
from routes.diet import diet_bp

app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Secret key for JWT

# Initialize extensions
db.init_app(app)
JWTManager(app)  # Initialize JWTManager here

# Initialize database
with app.app_context():
    db.create_all()

# Enable CORS
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(exercise_bp, url_prefix="/exercise")
app.register_blueprint(diet_bp, url_prefix="/diet")

# Define a root route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Fitness Tracker API!",
        "routes": {
            "/auth": "Authentication routes",
            "/exercise": "Exercise tracking routes",
            "/diet": "Diet tracking routes"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
