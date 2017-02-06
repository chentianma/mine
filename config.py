# -*- coding：utf-8 -*-

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'ivoryblog.db')
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'YOU-WILL-NEVER-GET'


class TestConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BOOTSTRAP_SERVE_LOCAL = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'YOU-WILL-NEVER-GET'