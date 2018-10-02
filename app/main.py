from flask import Flask
from flask import request

import json

from flask_api import FlaskAPI, status, exceptions
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://root:root@localhost:4000/test_db?authSource=admin"

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/stores')
def get_stores():
    request_args = request.args
    result = mongo.db.stores.find(request_args)
    result_str = json.dumps(list(result))
    return '{{"stores": {}}}'.format(result_str)

@app.route('/stores/<int:id>')
def get_store_by_id(id):
    request_args = request.args
    result = mongo.db.stores.find_one_or_404({"_id": id})
    result_str = json.dumps(result)
    return '{{"store": {}}}'.format(result_str)

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        request_args = request.args
        result = mongo.db.users.find(request_args)
        result_str = json.dumps(list(result))
        return '{{"users": {}}}'.format(result_str)
    elif request.method == 'POST':
        request_args = request.form
        if not request_args.get('_id'):
            return 'Bad request', status.HTTP_400_BAD_REQUEST
        if not request_args.get('name'):
            return 'Bad request', status.HTTP_400_BAD_REQUEST
        # ToDo: put stuff in db
        return 'GREAT', status.HTTP_200_OK

@app.route('/users/<int:id>')
def get_user_by_id(id):
    result = mongo.db.users.find_one_or_404({"_id": id})
    result_str = json.dumps(result)
    return '{{"user": {}}}'.format(result_str)

if __name__ == '__main__':
    app.run()
