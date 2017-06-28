# -*- coding: utf8 -*-


from flask import Blueprint
from config import basedir
import os


file = Blueprint('file', __name__,
                 template_folder='blog/templates',
                 static_folder= os.path.join(basedir, 'uploadFile'))

# from . import views, upload