#!/usr/bin/env python
# coding=utf-8
import datetime

from flask_mongoengine import MongoEngine

db = MongoEngine()


class User(db.EmbeddedDocument):
    email = db.StringField(required=True)
    name = db.StringField(max_length=50)
    password = db.StringField(required=True)
    active = db.BooleanField(default=True)
    isAdmin = db.BooleanField(default=False)
    timestamp = db.DateTimeField(default=datetime.datetime.now())