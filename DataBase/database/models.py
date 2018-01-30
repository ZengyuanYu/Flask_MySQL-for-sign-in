#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from exts import db

class Aritcle(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(100), nullable=False)