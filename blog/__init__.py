# -*- coding: utf8 -*-


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import *
from flask_wtf.csrf import CsrfProtect


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
# csrf = CsrfProtect()


def create_app(config='formal'):
    from .main import main as blog_blueprint
    from .api_1_0 import api as api_blueprint
    from .auth import auth as auth_blueprint
    app = Flask(__name__)
    app.config.from_object(configs[config])

    app.register_blueprint(blog_blueprint, url_prefix='/blog')
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    login_manager.init_app(app)
    bootstrap.init_app(app)
    # csrf.init_app(app)
    db.app = app
    db.init_app(app)
    db.create_all()
    return app
