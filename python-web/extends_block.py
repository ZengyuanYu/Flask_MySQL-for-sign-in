#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-26
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

class Person(object):
    name = 'heh'
    age = 0

class Student(Person):
    pass

@app.route('/')
def index():
    return render_template('index_extends.html')

@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
