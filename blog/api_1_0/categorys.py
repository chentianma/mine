# -*- coding: utf8 -*-


from . import api
from flask import request, jsonify
from blog import db
from ..models import User, Role, Article, Category


@api.route('/categorys', methods=['POST'])
def set_category():
    data = request.get_json()
    new_category = Category(name=data.name)
    db.session.add(new_category)
    db.session.commit()
    return jsonify(data)


@api.route('/category/<int:id>', methods=['GET'])
def get_category(id):
    cate = Category.query.filter_by(id=id).first()
    return jsonify(cate.to_json())


@api.route('/category/<int:id>/blogs', methods=['GET'])
def get_category_blogs(id):
    blogs = Article.query.filter_by(category_id=id).all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})