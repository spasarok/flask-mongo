import json

from flask import request
from flask_api import FlaskAPI, status, exceptions

from api.main import app
from api.utils.mongo import mongo

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
