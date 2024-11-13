from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', '27017'))
MONGO_DB = os.environ.get('MONGO_DB', 'mydatabase')
MONGO_USER = os.environ.get('MONGO_USER', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD
)

db = client[MONGO_DB]
users_collection = db['users']

def initialize_data():
    users_collection.insert_many([
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ])

initialize_data()

@app.route('/users', methods=['GET'])
def get_users():
    # Retrieve all users from the 'users' collection
    users = list(users_collection.find({}, {'_id': False}))
    return jsonify(users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
