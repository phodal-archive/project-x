#!/usr/bin/env python
# coding=utf-8
import datetime

from flask_mongoengine import MongoEngine
from mongoengine import ReferenceField, ListField
from users import User

db = MongoEngine()


class Tag(db.Document):
    name = db.StringField(max_length=50)
    description = db.StringField(max_length=300)
    timestamp = db.DateTimeField(default=datetime.datetime.now())


class Article(db.Document):
    description = db.StringField(max_length=300)
    tag = ListField(ReferenceField(Tag))
    title = db.StringField(max_length=10000)
    author = ListField(ReferenceField(User))
    create = db.DateTimeField(default=datetime.datetime.now())
    update = db.DateTimeField(default=datetime.datetime.now())