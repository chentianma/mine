# -*- coding: utf8 -*-


from flask import jsonify, redirect, request, url_for
from . import api
from blog import db
from ..models import User, Role, Article, Category
from flask_login import login_required
import json


@api.route('/blog/<int:id>')
def get_blog(id):
    blog = Article.query.filter_by(id=id).first()
    return jsonify({'blog': blog.to_json()})


@api.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Article.query.order_by(Article.pub_date.desc()).all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})


@api.route('/blog/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Article.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'Result': 'success'})


@api.route('/blog/edit/<int:id>')
@login_required
def edit_api(id):
    blog = Article.query.filter_by(id=id).first()
    return jsonify({'blog': blog.to_json()})


@api.route('/blog/<int:id>/edit', methods=['POST'])
@login_required
def edit_blog(id):
    title = request.form.get('title')
    text = request.form.get('text')
    des = request.form.get('description')
    # new_category = request.form.get('category')

    new_article = Article.query.filter_by(id=id).first()
    new_article.title = title
    new_article.text = text
    new_article.description =des
    # new_article.category_id = new_category
    new_id = id

    db.session.add(new_article)
    db.session.commit()
    return jsonify({'id': new_id})


@api.route('/blog/edit', methods=['POST'])
@login_required
def create_blog():
    title = request.form.get('title')
    text = request.form.get('text')
    des = request.form.get('description')
    category = request.form.get('category')

    user = User.query.filter_by(name='Admin1').first()
    cate = Category.query.filter_by(name=category).first()
    new_article = Article(title=title, description=des, text=text, user=user, category=cate)
    new_id = Article.query.filter_by(title=title).first_or_404().id

    db.session.add(new_article)
    db.session.commit()

    return jsonify({'id': new_id})
