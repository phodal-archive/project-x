#!/usr/bin/env python
# coding=utf-8
import datetime

from flask_mongoengine import MongoEngine

db = MongoEngine()


class Tag(db.Document):
    name = db.StringField(max_length=50)
    description = db.StringField(max_length=300)
    timestamp = db.DateTimeField(default=datetime.datetime.now())


class Article(db.Document):
    name = db.StringField(max_length=50)
    description = db.StringField(max_length=300)
    tag = db.StringField(max_length=300)
    title = db.StringField(max_length=10000)
    user = db.StringField(max_length=10000)
    create = db.DateTimeField(default=datetime.datetime.now())
    update = db.DateTimeField(default=datetime.datetime.now())