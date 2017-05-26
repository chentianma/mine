# -*- coding: utf8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import login_manager
from flask import url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(UserMixin, db.Model):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(100))
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))
    article = db.relationship('Article', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        # return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.name


class Role(db.Model):

    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.role


class Article(db.Model):

    __tablename__ = 'Article'

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(100), default='44.jpg')
    title = db.Column(db.String(100))
    description = db.Column(db.String(150))
    text = db.Column(db.Text)
    text_html = db.Column(db.Text)
    pub_date = db.Column(db.DateTime, default=datetime.now())
    click = db.Column(db.Integer, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))

    def parse_description(self):
        keys = [key for key in self.description.split(';')]
        return keys

    def to_json(self):
        c = Category.query.get_or_404(self.category_id).name
        oc = Category.query.filter(Category.name != c).all()
        other_category = []
        for i in oc:
            other_category.append(i.name)
        # print(other_category)
        # u = User.query.get_or_404(self.author_id).name
        # u = self.user.name
        blog_json = {
            'id': self.id,
            'url': url_for('main.single_blog',
                           id=self.id,
                           _external=True),
            'title': self.title,
            'text': self.text,
            'description': self.description,
            'descriptions': self.parse_description(),
            'time': self.pub_date,
            'html': self.text_html,
            # 'user': u,
            'category': c,
            'other_category': other_category,
            'img_url': url_for('static', filename='article_img/%s' % self.img, _external=True)
        }
        return blog_json

    def __repr__(self):
        return '<Article %r>' % self.title


class Category(db.Model):

    __tablename__ = 'Category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    articles = db.relationship('Article', backref='category',
                               lazy='dynamic')

    def to_json(self):
        cate_json = {
            'url': url_for('api.get_category',
                           id=self.id,
                           _external=True),
            'name': self.name,
            'articles': url_for('main.category_blogs',
                                id=self.id,
                                _external=True)
        }
        return cate_json

    def __repr__(self):
        return '<Category %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(int(user_id))
