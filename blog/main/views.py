# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app
from flask_login import login_required
from . import main
from blog import db
from ..models import User, Role, Article, Category, Topic


@main.route('/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.filter_by(isDeleted=False, isPublished=True).order_by(
        Article.pub_date.desc()).paginate(
        page, per_page=current_app.config['FLASKY_BLOGS_PER_PAGE'],
        error_out=False)
    blogs = pagination.items
    categorys = Category.query.filter_by(isDeleted=False).all()
    categorys_dict = {}
    for i in categorys:
        categorys_dict[i.id] = i.name
    # print(categorys_dict)
    return render_template('main/index.html', blogs=blogs,
                           pagination=pagination, categorys_dict=categorys_dict)


@main.route('/<int:id>', methods=['GET'])
def single_blog(id):
    blog = Article.query.filter_by(isDeleted=False,isPublished=True, id=id).first_or_404()
    return render_template('main/blog.html')


@main.route('/category/<int:id>/blogs', methods=['GET'])
def category_blogs(id):
    category = Category.query.filter_by(isDeleted=False, id=id).first_or_404()
    blogs = Article.query.filter_by(isDeleted=False, isPublished=True, category_id=id).all()
    return render_template('main/category.html', blogs=blogs, category=category)


@main.route('/topic/<int:id>/blogs', methods=['GET'])
def topic_blogs(id):
    topic = Topic.query.filter_by(isDeleted=False, id=id).first_or_404()
    category = Category.query.get(topic.category_id).name
    blogs = Article.query.filter_by(isDeleted=False, isPublished=True, topic_id=id).all()
    return render_template('main/topic.html', blogs=blogs, topic=topic, category=category)


@main.route('/cms', methods=['GET'])
@login_required
def cms():
    blogs = Article.query.filter_by(isDeleted=False).all()
    return render_template('main/cms.html', blogs=blogs)


@main.route('/new', methods=['GET'])
@login_required
def new():
    categorys = Category.query.filter_by(isDeleted=False).all()
    return render_template('main/new.html', categorys=categorys)


@main.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit(id):
    return render_template('main/edit.html')


@main.route('/about', methods=['GET'])
def about():
    return render_template('main/about.html')
