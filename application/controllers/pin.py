#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from .site import bp
from ..models import db, Author, Page, Pic


@bp.route('/pin', methods=['GET'])
def pin():
    """投递页"""
    return render_template('site/pin.html')
