#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-31
import os
DEBUG = True

SECRET_KEY = os.urandom(24)

#dialect+drive://username:password@host:port/database
DIALECT = 'mysql'
DRIVE = 'mysqldb'
USERNAME = 'root'
PASSWORD = '272617'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa_demo'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVE,
                                                    USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False