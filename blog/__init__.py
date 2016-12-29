# -*- coding: utf8 -*-


from flask import Flask


def create_app():
    from .main import main as blog_blueprint
    app = Flask(__name__)
    app.register_blueprint(blog_blueprint)
    return app
