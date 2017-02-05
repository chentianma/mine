# -*- coding: utf8 -*-


from flask import Blueprint


main = Blueprint('main', __name__,
                 template_folder='blog/templates',
                 static_folder='blog/static')

from . import views