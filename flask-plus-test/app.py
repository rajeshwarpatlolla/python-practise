from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

app = Flask(__name__)
api = Api(app)

db = MongoClient(
    "mongodb://admin123:admin123@ds257507.mlab.com:57507/python-db?authSource=python-db&retryWrites=false").get_database()


class Users(Resource):
    def get(self):
        users = db.users.find()
        return json.loads(dumps(users))

    def post(self):
        user = db.users.insert(request.json)
        return json.loads(dumps(user))


class User(Resource):
    def get(self, user_id):
        user_data = db.users.find_one({"_id": ObjectId(user_id)})
        return json.loads(dumps(user_data))

    def put(self, user_id):
        updated_user = db.users.update({"_id": ObjectId(user_id)}, request.json)
        return json.loads(dumps(updated_user))

    def delete(self, user_id):
        deleted_user = db.users.remove({"_id": ObjectId(user_id)})
        return json.loads(dumps(deleted_user))


api.add_resource(Users, '/users')
api.add_resource(User, '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)
