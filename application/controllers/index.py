#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from .site import bp
from ..models import db, Author, Page, Pic


@bp.route('/', methods=['GET'])
def index():
    """首页"""
    return render_template('site/index.html')
