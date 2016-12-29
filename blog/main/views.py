# -*- coding: utf8 -*-


from flask import render_template
from . import main


@main.route('/', methods=['GET'])
def index():
    return '<h1>Hello world!</h1>'
