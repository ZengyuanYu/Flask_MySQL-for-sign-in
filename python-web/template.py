#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 2018/1/23

from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    class Person(object):
        name=u'haha'
        age = 18
    p = Person()

    context = {
        'username': u'hehe',
        'gender': u'man',
        'age': u'18',
        'person': p,
        'websites':{
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)

