#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from flask import Flask, session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# 添加数据到session

@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    return 'Hello World!'

@app.route('/get/')
def get():
    return session.get('username')

@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'

@app.route('/clear/')
def clear():
    print(session.get('username'))
    session.clear()
    print(session.get('username'))
    return 'success'
if __name__ == '__main__':
    app.run(debug=True)
