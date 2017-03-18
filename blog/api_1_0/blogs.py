# -*- coding: utf8 -*-


from flask import jsonify, redirect, request, url_for
from . import api
from blog import db, User, Role, Article, Category
import json


@api.route('/api/blog/<int:id>')
def get_blog(id):
    blog = Article.query.filter_by(id=id).first()
    return jsonify({'blog': blog.to_json()})


@api.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = Article.query.all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})


@api.route('/api/blog/<int:id>/delete', methods=['GET', 'POST'])
def delete_blog(id):
    blog = Article.query.filter_by(id=id).first_or_404()
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'Result': 'success'})


@api.route('/api/blog/edit/<int:id>')
def edit_api(id):
    blog = Article.query.filter_by(id=id).first()
    return jsonify({'blog': blog.to_json()})


@api.route('/api/blog/<int:id>/edit', methods=['POST'])
def edit_blog(id):
    title = request.form.get('title')
    text = request.form.get('text')

    new_article = Article.query.filter_by(id=id).first()
    new_article.title = title
    new_article.text = text
    new_id = id

    db.session.add(new_article)
    db.session.commit()
    return jsonify({'id': new_id})


@api.route('/api/blog/edit', methods=['POST'])
def create_blog():
    title = request.form.get('title')
    text = request.form.get('text')

    user = User.query.filter_by(name='Admin1').first()
    cate = Category.query.filter_by(name='Python').first()
    new_article = Article(title=title, text=text, user=user, category=cate)
    new_id = Article.query.filter_by(title=title).first_or_404().id

    db.session.add(new_article)
    db.session.commit()

    return jsonify({'id': new_id})
