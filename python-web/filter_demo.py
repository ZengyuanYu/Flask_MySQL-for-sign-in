#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-26
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    comments = [
        {
            'user': u'zihiele',
            'content': 'xxxx'
        },
        {
            'user': u'heheheh',
            'content': 'xxx'
        }
    ]
    return render_template('index_filter.html', comments=comments)
if __name__ == '__main__':
    app.run()
