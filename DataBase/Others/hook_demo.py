#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    return 'login'

@app.before_request
def my_before_request():
    print('hello world')

if __name__ == '__main__':
    app.run(debug=True)
