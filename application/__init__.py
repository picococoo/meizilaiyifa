#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# 将project目录加入sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from flask import Flask, request, url_for, g, render_template, session
from flask_wtf.csrf import CsrfProtect
from config import load_config

# convert python's encoding to utf8
reload(sys)
sys.setdefaultencoding('utf-8')


def create_app():
    app = Flask(__name__)

    config = load_config()
    app.config.from_object(config)
    app.logger.addHandler(config.mail_handler)

    # CSRF protect
    CsrfProtect(app)

    # 注册组件
    register_db(app)
    register_routes(app)
    register_jinja(app)
    register_error_handle(app)

    return app


def register_jinja(app):
    """注册模板全局变量和全局函数"""
    from jinja2 import Markup
    from .utils import filters

    app.jinja_env.filters['timesince'] = filters.timesince

    # inject vars into template context
    @app.context_processor
    def inject_vars():
        return dict(
            g_var=0
        )

    def url_for_other_page(page):
        """Generate url for pagination"""
        view_args = request.view_args.copy()
        args = request.args.copy().to_dict()
        combined_args = dict(view_args.items() + args.items())
        combined_args['page'] = page
        return url_for(request.endpoint, **combined_args)

    def static(filename):
        """静态资源url"""
        return url_for('static', filename=filename)

    def script(path):
        """script标签"""
        return Markup("<script type='text/javascript' src='%s'></script>" % static(path))

    def link(path):
        """link标签"""
        return Markup("<link rel='stylesheet' href='%s'>" % static(path))

    def page_script(template_reference):
        """单页script标签"""
        template_name = _get_template_name(template_reference)
        return script('js/%s' % template_name.replace('html', 'js'))

    def page_link(template_reference):
        """单页link标签"""
        template_name = _get_template_name(template_reference)
        return link('css/%s' % template_name.replace('html', 'css'))

    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
    app.jinja_env.globals['static'] = static
    app.jinja_env.globals['script'] = script
    app.jinja_env.globals['page_script'] = page_script
    app.jinja_env.globals['link'] = link
    app.jinja_env.globals['page_link'] = page_link


def register_db(app):
    """注册Model"""
    from .models import db

    db.init_app(app)


def register_routes(app):
    """注册路由"""
    from .controllers import site

    app.register_blueprint(site.bp, url_prefix='')


def register_error_handle(app):
    """注册HTTP错误页面"""

    @app.errorhandler(403)
    def page_403(error):
        return render_template('site/403.html'), 403

    @app.errorhandler(404)
    def page_404(error):
        return render_template('site/404.html'), 404

    @app.errorhandler(500)
    def page_500(error):
        return render_template('site/500.html'), 500


def _get_template_name(template_reference):
    """获取当前模板名"""
    return template_reference._TemplateReference__context.name
