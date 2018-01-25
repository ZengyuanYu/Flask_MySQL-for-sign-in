#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 2018/1/23
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/<is_login>/')
def index(is_login):
    if is_login == '1':
        user = {
            'username': u'heheh',
            'age': 20,
        }
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()

