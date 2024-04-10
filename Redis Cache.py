import json
import requests
from flask import Flask, jsonify
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)

def fetch_user_data(user_id):
    user_data = r.get(user_id)
    if user_data is None:
        response = requests.get(f'http://localhost:5000/api/users/{user_id}')
        user_data = response.json()
        r.set(user_id, json.dumps(user_data))

    return user_data

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = fetch_user_data(user_id)
    return jsonify(user_data)

if __name__ == '__main__':
    app.run()
