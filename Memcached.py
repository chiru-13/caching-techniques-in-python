import json
import requests
from flask import Flask, jsonify
import memcache

mc = memcache.Client(['localhost:11211'])

app = Flask(__name__)

def fetch_user_data(user_id):
    user_data = mc.get(user_id)
    if user_data is None:
        response = requests.get(f'http://localhost:5000/api/users/{user_id}')
        user_data = response.json()
        mc.set(user_id, json.dumps(user_data))

    return user_data

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = fetch_user_data(user_id)
    return jsonify(user_data)

if __name__ == '__main__':
    app.run()
