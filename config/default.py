#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Config(object):
    """配置基类"""
    # Flask app config
    DEBUG = False
    TESTING = False

    JSON_AS_ASCII = False

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # SQLAlchemy config
    # See:
    # https://pythonhosted.org/Flask-SQLAlchemy/config.html#connection-uri-format
    # http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s/db/testing.db" % PROJECT_PATH
