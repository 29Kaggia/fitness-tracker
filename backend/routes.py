from flask import Flask, request, jsonify
from models import db, DietLog

app = Flask(__name__)

@app.route('/diet/', methods=['GET', 'POST'])
def diet_logs():
    if request.method == 'GET':
        # Fetch all diet logs
        logs = DietLog.query.all()
        return jsonify({"logs": [log.to_dict() for log in logs]})

    if request.method == 'POST':
        # Add a new diet log
        data = request.json
        food_item = data.get('food_item')
        calories = data.get('calories')
        date = data.get('date')

        if not (food_item and calories and date):
            return jsonify({"error": "Missing fields"}), 400

        new_log = DietLog(food_item=food_item, calories=calories, date=date)
        db.session.add(new_log)
        db.session.commit()

        return jsonify(new_log.to_dict()), 201
