#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def load_config():
    """加载配置类"""
    mode = os.environ.get('SERVER_SOFTWARE')
    try:
        if mode is None:
            from .development import DevelopmentConfig
            return DevelopmentConfig
        else:
            from .production import ProductionConfig
            return ProductionConfig
    except ImportError, e:
        from .default import Config
        return Config
