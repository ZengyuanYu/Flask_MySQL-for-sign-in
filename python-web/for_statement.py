#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-25
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

#for遍历字典
# @app.route('/')
# def index():
#     user = {
#         'username': u'hehe',
#         'age': 18,
#     }
#
#     websites = ['baidu.com', 'google.com']
#     return render_template('index_for.html',user=user, websites=websites)


@app.route('/')
def index():
    books =[
        {
            'name': u'西游记',
            'author': u'吴承恩',
            'price': 109
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price': 120
        },
        {
            'name': u'红楼梦',
            'author': u'曹雪芹',
            'price': 180
        },
        {
            'name': u'水浒传',
            'author': u'施耐庵',
            'price': 100
        }
    ]
    return render_template('index_for_plus.html', books=books)

if __name__ == '__main__':
    app.run()

