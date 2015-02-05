#!/usr/bin/env python
# coding=utf-8
import datetime

from flask_mongoengine import MongoEngine
from mongoengine import ListField, EmbeddedDocumentField

from xunta.users.models import User

db = MongoEngine()


class Tag(db.EmbeddedDocument):
    name = db.StringField(max_length=50)
    description = db.StringField(max_length=300)
    timestamp = db.DateTimeField(default=datetime.datetime.now())


class Article(db.Document):
    description = db.StringField(max_length=300)
    tag = ListField(EmbeddedDocumentField(Tag))
    title = db.StringField(max_length=10000)
    content = db.StringField(max_length=300)
    author = ListField(EmbeddedDocumentField(User))
    create = db.DateTimeField(default=datetime.datetime.now())
    update = db.DateTimeField(default=datetime.datetime.now())