# -*- coding: utf8 -*-


from flask import jsonify, redirect
from . import api
from blog import db, User, Role, Article, Category


@api.route('/api/blog/<int:id>')
def get_blog(id):
    blog = Article.query.filter_by(id=id).first()
    return jsonify(blog.to_json())


@api.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = Article.query.all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})


@api.route('/api/blog/delete/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):
    blog = Article.query.filter_by(id=id).first_or_404()
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'Result': 'success'})
