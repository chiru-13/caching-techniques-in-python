import json
import requests
from flask import Flask, jsonify
from flask_caching import Cache

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=300, key_prefix='user_data')
def fetch_user_data(user_id):
    response = requests.get(f'http://localhost:5000/api/users/{user_id}')
    return response.json()

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = fetch_user_data(user_id)
    return jsonify(user_data)

if __name__ == '__main__':
    app.run()
