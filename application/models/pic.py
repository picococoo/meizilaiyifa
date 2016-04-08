#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from ._base import db
from .page import Page


class Pic(db.Model):
    __tablename__ = 'pic'
    id = db.Column(db.Integer, primary_key=True)
    md5 = db.Column(db.String(32))
    url = db.Column(db.String(100))
    downloaded = db.Column(db.Boolean)
    origin = db.Column(db.String(100), db.ForeignKey('page.ref'))
    origin_md5 = db.Column(db.String(32))
    page = db.relationship(Page)

    def __repr__(self):
        return '<Pic %r>' % self.md5
