# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app
from flask_login import login_required
from . import main
from blog import db
from ..models import User, Role, Article, Category
from flask_uploads import *
