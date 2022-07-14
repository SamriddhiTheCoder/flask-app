import jsonify
from flask import Flask
import requests

contacts = []

{
    "data": [
        {
            'Contact': '9898989890',
            'Name': 'Ri',
            'done': False,
            'id': 1
        },
        {
            'Contact': '9876543210',
            'Name': 'Ad',
            'done': False,
            'id': 2
        },
    ]
}

app = Flask(__name__)
@app.route("/add-data", methods=["POST"])

def add_task():
    if not requests.json:
        return jsonify({
            'status': 'error',
            'message': 'Please provide the data.'
        }, 400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': requests.json['Name'],
        'Contact': requests.json.get('Contact', ""),
        'done': False
    }

    contacts.append(contact)

if(__name__ == "__main__"):
    app.run()