#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('site', __name__)

from .index import *
from .topic import *
from .pin import *
from .about import *
from .api import *