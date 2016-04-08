#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from .site import bp
from ..models import db, Author, Page, Pic


@bp.route('/about', methods=['GET'])
def about():
    """关于页"""
    return render_template('site/about.html')
