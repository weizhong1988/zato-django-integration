# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# stdlib
import os, sys
from wsgiref.simple_server import make_server

# Django
from django.core.handlers.wsgi import WSGIHandler

settings_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, settings_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

app = WSGIHandler()
make_server('127.0.0.1', 8188, app).serve_forever()
