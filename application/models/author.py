#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from ._base import db


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50))
    author_page = db.Column(db.String(100))

    def __repr__(self):
        return '<Author %r>' % self.author_name
