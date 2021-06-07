import json
from flask import Flask, request
from db import SQLiteConnection

app = Flask(__name__)
sqlite_connection = SQLiteConnection()


@app.route('/api/add_to_favorites', methods=['POST'])
def add_to_favorites():
    data = json.loads(request.data)
    sqlite_connection.save_to_favorites(data)
    return {}


@app.route('/get_favorites', methods=['GET'])
def get_favorites():
    return json.dumps(sqlite_connection.get_list_of_favorites())
