#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging import Formatter
from logging.handlers import SMTPHandler

from .default import Config

from sae.const import (MYSQL_HOST, MYSQL_PORT,
            MYSQL_USER, MYSQL_PASS, MYSQL_DB)


class ProductionConfig(Config):
    # App config
    DEBUG = False
    TESTING = False

    # Disable csrf while testing
    WTF_CSRF_ENABLED = True

    # Db config
    SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{host}:{port}/{db}".format(
        user=MYSQL_USER,
        password=MYSQL_PASS,
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        db=MYSQL_DB)
        
    SQLALCHEMY_POOL_RECYCLE = 10                                                                          

    #: logging config
    ADMINS = ['hackzhuyan@gmail.com']
    credentials = ('hackzhuyan@163.com', 'gameover')
    mail_handler = SMTPHandler(('smtp.163.com', 25),
                               'server-error@meizilaiyifa',
                               ADMINS, 'YourApplication Failed', credentials)
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(Formatter('''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    '''))
