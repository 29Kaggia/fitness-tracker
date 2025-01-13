import sqlite3
from models import db

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercise_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        activity TEXT,
        duration INTEGER,
        date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diet_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        food_item TEXT,
        calories INTEGER,
        date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")
    conn.commit()
    conn.close()
