# -*- coding: utf8 -*-


from . import api
from flask import request, jsonify, redirect
from blog import db
from ..models import User, Role, Article, Category
from flask_login import login_required


@api.route('/setCategory', methods=['POST'])
@login_required
def set_category():
    data = request.form['newC']
    new_category = Category(name=data)
    db.session.add(new_category)
    db.session.commit()
    return redirect('/blog')


@api.route('/category/<int:id>', methods=['GET'])
def get_category(id):
    cate = Category.query.filter_by(id=id).first()
    return jsonify(cate.to_json())


@api.route('/categories', methods=['GET'])
def get_categories():
    cates = Category.query.all()
    return jsonify({'categories': [cate.to_json() for cate in cates]})


@api.route('/category/<int:id>/blogs', methods=['GET'])
def get_category_blogs(id):
    blogs = Article.query.filter_by(category_id=id).all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})