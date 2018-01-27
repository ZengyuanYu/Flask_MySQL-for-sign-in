#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-26
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index_url.html')

@app.route('/login/')
def login():
    return render_template('login_url.html')
if __name__ == '__main__':
    app.run()
