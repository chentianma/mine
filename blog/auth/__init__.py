
from flask import Blueprint


auth = Blueprint('auth', __name__,
                 template_folder='blog/templates',
                 static_folder='blog/static')

from . import views