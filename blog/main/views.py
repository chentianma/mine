# -*- coding: utf8 -*-


from flask import render_template, flash
from . import main
from blog import db, User, Role, Article, Category


@main.route('/blog', methods=['GET'])
def index():
    blogs = Article.query.all()
    flash("进这里是首页！！")
    return render_template('main/index.html', blogs=blogs)


@main.route('/blog/<int:id>', methods=['GET'])
def single_blog(id):
    blog = Article.query.filter_by(id=id).first_or_404()
    return render_template('main/blog.html', blog=blog)


@main.route('/blog/category', methods=['GET'])
def category():
    return render_template('main/category.html')


@main.route('/blog/cms', methods=['GET'])
def cms():
    blogs = Article.query.all()
    return render_template('main/cms.html', blogs=blogs)


@main.route('/blog/new', methods=['GET'])
def new():
    return render_template('main/new.html')


@main.route('/blog/edit/<int:id>', methods=['GET'])
def edit(id):
    return render_template('main/edit.html')