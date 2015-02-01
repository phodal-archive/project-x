from flask_mongoengine import MongoEngine

db = MongoEngine()


class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
