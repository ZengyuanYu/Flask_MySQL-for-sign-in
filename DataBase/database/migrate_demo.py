#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from flask import Flask
from exts import db
import config
from models import Aritcle

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# with app.app_context():
#     db.create_all()
@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()
