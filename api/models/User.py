# from flask_mongoengine.wtf import model_form

from api.utils.mongo import db

class User(db.Document):
    _id = db.IntField(required=True)
    name = db.StringField(required=True, max_length=50)
    meta = {'collection': 'users'}

# PostForm = model_form(User)
