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


@api.route('/deleteCategory/<int:id>', methods=['POST'])
@login_required
def delete_category(id):
    category = Category().query.get(id)
    if category.isDeleted:
        return {'status': 200}
    else:
        category.isDeleted = True
        db.session.add(category)
        db.session.commit()
        # return redirect('/blog')
        return {'status': 200}


@api.route('/category/<int:id>', methods=['GET'])
def get_category(id):
    cate = Category.query.filter_by(isDeleted=False, id=id).first_or_404()
    return jsonify(cate.to_json())


@api.route('/categories', methods=['GET'])
def get_categories():
    cates = Category.query.filter_by(isDeleted=False).all()
    return jsonify({'categories': [cate.to_json() for cate in cates]})


@api.route('/category/<int:id>/blogs', methods=['GET'])
def get_category_blogs(id):
    blogs = Article.query.filter_by(isDeleted=False, category_id=id).all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})