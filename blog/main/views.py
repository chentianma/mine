# -*- coding: utf8 -*-


from flask import render_template
from . import main
from blog import db, User, Role, Article, Category


@main.route('/index', methods=['GET'])
def index():
    blogs = Article.query.all()
    return render_template('main/index.html', blogs=blogs)


@main.route('/blog/<int:id>', methods=['GET'])
def single_blog(id):
    blog = Article.query.filter_by(id=id).first_or_404()
    return render_template('main/blog.html', blog=blog)


@main.route('/category', methods=['GET'])
def category():
    return render_template('main/category.html')


@main.route('/cms', methods=['GET'])
def cms():
    blogs = Article.query.all()
    return render_template('main/cms.html', blogs=blogs)