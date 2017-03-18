# -*- coding: utf8 -*-


from flask import Flask
from flask_bootstrap import Bootstrap
from config import *
from .models import User, Role, Article, Category, db


# bootstrap = Bootstrap()


def create_app():
    from .main import main as blog_blueprint
    from .api_1_0 import api as api_blueprint
    app = Flask(__name__)
    app.config.from_object(TestConfig())

    app.register_blueprint(blog_blueprint)
    app.register_blueprint(api_blueprint)

    db.app = app
    db.init_app(app)
    db.create_all()
    return app
