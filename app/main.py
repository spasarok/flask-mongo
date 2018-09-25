from flask import Flask
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://root:root@localhost:4000/test_db?authSource=admin"

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/stores')
def get_stores():
    result = mongo.db.stores.find()
    result_str = json.dumps(list(result))
    return '"stores": {}'.format(result_str)

@app.route('/stores/id/<int:id>')
def get_stores_by_id(id):
    result = mongo.db.stores.find({"_id": id})
    result_str = json.dumps(list(result))
    return '"stores": {}'.format(result_str)

@app.route('/users')
def get_users():
    result = mongo.db.users.find()
    result_str = json.dumps(list(result))
    return '"users": {}'.format(result_str)

if __name__ == '__main__':
    app.run()
