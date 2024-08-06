from flask import Flask, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient
app = Flask(__name__)


db = MongoClient(
    "mongodb://admin123:admin123@ds257507.mlab.com:57507/python-db?authSource=python-db").get_database()

print(db.collection_names())


@app.route('/users')
def get_all_users():
    # to access query params /users?user_id="12345"
    # print(request.args.get('user_id'), request.query_string)
    # Output is: "12345", b'user_id=%2212345%22'
    users_list = db.users.find()
    # print(users_list)
    # Output is: <pymongo.cursor.Cursor object at 0x11124b278>
    return dumps(users_list)


@app.route('/users/<user_id>', methods=["GET"])
def get_user_details(user_id):
    user_data = db.users.find_one({"_id": ObjectId(user_id)})
    return dumps(user_data)


@app.route('/users', methods=["POST"])
def create_user():
    new_user = db.users.insert(request.json)
    return dumps(new_user)


@app.route('/users/<user_id>', methods=["PUT"])
def update_user_details(user_id):
    updated_user = db.users.update({"_id": ObjectId(user_id)}, request.json)
    return dumps(updated_user)


@app.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    deleted_user = db.users.remove({"_id": ObjectId(user_id)})
    return dumps(deleted_user)


if __name__ == '__main__':
    app.run(debug=True)
