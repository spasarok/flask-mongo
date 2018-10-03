import json

from flask import request
from flask_api import FlaskAPI, status, exceptions

from api.main import app
from api.utils.mongo import mongo
from api.controllers.users import get_users, get_user_by_id, post_user

@app.route('/users', methods=['GET', 'POST'])
def users(id=None):
    if request.method == 'GET':
        return get_users(request.args)
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
