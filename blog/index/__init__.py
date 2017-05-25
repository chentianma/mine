# -*- coding: utf8 -*-


from flask import Blueprint


index = Blueprint('index', __name__,
                 template_folder='blog/templates',
                 static_folder='blog/static')

from . import views