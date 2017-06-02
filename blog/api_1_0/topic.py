# -*- coding: utf8 -*-


import os
from flask import jsonify, redirect, request, url_for, flash
from . import api
from blog import db
from ..models import User, Role, Article, Category, Topic
from flask_login import login_required
import json


@api.route('/topics')
def get_topics():
    topics = Topic.query.filter_by(isDeleted=False).all()
    return jsonify({'topics': [topic.to_json() for topic in topics]})


@api.route('/topic/<int:id>/blogs', methods=['GET'])
def get_topic_blogs(id):
    blogs = Article.query.filter_by(isDeleted=False, topic_id=id).all()
    return jsonify({'blogs': [blog.to_json() for blog in blogs]})


@api.route('/setTopic', methods=['POST'])
@login_required
def set_topic():
    title = request.form['newT']
    description = request.form['description']
    category = request.form['category']
    category_ob = Category.query.filter_by(name=category).first()
    if not category_ob:
        flash('分类名不存在！')
        return redirect('/blog')
    else:
        category_id = category_ob.id
        print(category_id)
        new_topic = Topic(title=title, description=description, category_id=category_id)
        db.session.add(new_topic)
        db.session.commit()
        return redirect('/blog')