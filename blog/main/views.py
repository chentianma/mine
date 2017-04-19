# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app
from flask_login import login_required
from . import main
from blog import db
from ..models import User, Role, Article, Category


@main.route('/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.pub_date.desc()).paginate(
        page, per_page=current_app.config['FLASKY_BLOGS_PER_PAGE'],
        error_out=False)
    blogs = pagination.items
    return render_template('main/index.html', blogs=blogs, pagination=pagination)


@main.route('/<int:id>', methods=['GET'])
def single_blog(id):
    blog = Article.query.filter_by(id=id).first_or_404()
    return render_template('main/blog.html')


@main.route('/category', methods=['GET'])
def category():
    return render_template('main/category.html')


@main.route('/cms', methods=['GET'])
@login_required
def cms():
    blogs = Article.query.all()
    return render_template('main/cms.html', blogs=blogs)


@main.route('/new', methods=['GET'])
@login_required
def new():
    return render_template('main/new.html')


@main.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit(id):
    return render_template('main/edit.html')


@main.route('/about', methods=['GET'])
def about():
    return render_template('main/about.html')
