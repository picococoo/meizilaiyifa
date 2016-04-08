#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re
from flask import render_template, json, jsonify, request, make_response
from .site import bp
from ..models import db, Author, Page, Pic


@bp.route('/api/topic/', defaults={'page_num': 0}, methods=['GET'])
@bp.route('/api/topic/<int:page_num>', methods=['GET'])
def api_topic(page_num):
    """首页数据接口"""
    rand_offset = random.randint(1, 800)
    default_show_nums = 18
    db_session = db.create_scoped_session()
    index_topic_list = db_session.query(Page.ref_md5, Page.title, Pic.md5)\
                                 .filter(Pic.origin_md5 == Page.ref_md5)\
                                 .group_by(Page.ref)\
                                 .offset(rand_offset + page_num * default_show_nums)\
                                 .limit(default_show_nums)\
                                 .all()
    db_session.remove()
    rs = [dict({'title': i[1].encode('utf-8'), 'ref': i[0], 'thumb': i[2]}) for i in index_topic_list]

    return jsonify({'topics': rs}), 200


@bp.route('/api/detail/<string:topic_md5>', methods=['GET'])
def api_detail(topic_md5):
    """详细页数据接口"""
    m = re.match('^\w{32}$', topic_md5)
    if m:
        db_session = db.create_scoped_session()
        rs = db_session.query(Pic.md5)\
                       .filter(Pic.origin_md5 == topic_md5)\
                       .all()
        title = db_session.query(Page.title)\
                          .filter(Page.ref_md5 == topic_md5)\
                          .first()
        db_session.remove()
        rs = [dict({'link': i[0]}) for i in rs]
        return jsonify({'pics': rs, 'title': title}), 200
    else:
        return jsonify({'error': 'invalid topic'}), 400
