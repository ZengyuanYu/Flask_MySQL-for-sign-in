#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    q = request.args.get('q')
    return u'用户提交的查询参数是： %s' % q
#
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username: %s' % username)
        print('password: %s' % password)
        return 'done'

if __name__ == '__main__':
    app.run(debug=True)
