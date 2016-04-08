#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from .site import bp
from ..models import db, Author, Page, Pic


@bp.route('/t/<topic_id>', methods=['GET'])
def topic(topic_id):
    """主题"""
    return render_template('site/topic.html', topic_id=topic_id)
