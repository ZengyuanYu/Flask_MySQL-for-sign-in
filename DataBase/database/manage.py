#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from flask_script import Manager
from flask_script_demo import app
from db_script import DBmanager

manager = Manager(app)

@manager.command
def runserver():
    print('服务器跑起来了！')

manager.add_command('db', DBmanager)

if  __name__ == '__main__':
    manager.run()