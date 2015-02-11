#!/usr/bin/env python
# coding=utf-8
import datetime

from flask_mongoengine import MongoEngine
from mongoengine import ReferenceField

from xunta.users.models import User

db = MongoEngine()


class Tag(db.Document):
    name = db.StringField(max_length=50)
    description = db.StringField(max_length=300)
    timestamp = db.DateTimeField(default=datetime.datetime.now())


class Article(db.DynamicDocument):
    description = db.StringField(max_length=300)
    tag = ReferenceField(Tag)
    slug = db.StringField(max_length=255, required=True)
    title = db.StringField(max_length=10000)
    content = db.StringField(max_length=300)
    author = ReferenceField(User)
    create = db.DateTimeField(default=datetime.datetime.now())
    update_at = db.DateTimeField(default=datetime.datetime.now())


class Vote(db.EmbeddedDocument):
    user = ReferenceField(User, required=True)
    up = db.BooleanField(required=True, default=True)


class Comment(db.Document):
    article = ReferenceField(Article)
    content = db.StringField(max_length=300)
    user = ReferenceField(User)
    vote = db.IntField(required=True, default=0)
    # votes = db.ListField(EmbeddedDocumentField(Vote))
    created_at = db.DateTimeField(default=datetime.datetime.now())