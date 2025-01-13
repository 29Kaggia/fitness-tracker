from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DietLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_item = db.Column(db.String(120), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "food_item": self.food_item,
            "calories": self.calories,
            "date": self.date,
        }
