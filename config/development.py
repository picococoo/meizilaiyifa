#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .default import Config


class DevelopmentConfig(Config):
    # App config
    TESTING = True
    DEBUG = True

    # Disable csrf while testing
    WTF_CSRF_ENABLED = False

    # Db config
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s/db/girls.db" % Config.PROJECT_PATH
