#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from ._base import db
from .author import Author


class Page(db.Model):
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    ref = db.Column(db.String(100))
    ref_md5 = db.Column(db.String(32))
    visited = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship(Author)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Page %r>' % self.title
