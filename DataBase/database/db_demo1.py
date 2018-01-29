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

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

db.create_all()
@app.route('/')
def index():
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()

    article = Article(title='aaa', content='bbb', author_id=1)
    db.session.add(article)
    db.session.commit()
    return 'index'


if __name__ == '__main__':
    app.run()
