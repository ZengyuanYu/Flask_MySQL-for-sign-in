#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-28
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

#用户表

#文章表

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    #password = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('articles'))
db.create_all()
@app.route('/')
def index():
    #添加一个用户
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()

    #由外键创建内容
    # article = Article(title="aaa", content="bb", author_id=1)
    # db.session.add(article)
    # db.session.commit()

    #文章标题为aaa的作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print(user.username)

    # article = Article(title='aaa', content='bbb')
    # article.author = User.query.filter(User.id == 1).first()
    # db.session.add(article)
    # db.session.commit()

    # article = Article.query.filter(Article.title == 'aaa').first()
    # print('username: %s' % article.author.username)

    # article = Article(title='111', content='222', author_id=1)
    # db.session.add(article)
    # db.session.commit()
    user = User.query.filter(User.username == 'zhiliao').first()
    result = user.articles
    for article in result:
        print('-'*10)
        print(article.title)
    return 'index'


if __name__ == '__main__':
    app.run()
