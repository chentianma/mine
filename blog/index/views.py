# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app, redirect
from flask_login import login_required
from . import index
from blog import db
from ..models import User, Role, Article, Category


@index.route('/', methods=['GET'])
def index():
    return redirect('/blog')
