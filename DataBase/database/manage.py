#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-30
from flask_script import Manager
from migrate_demo import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
# from db_script import DBmanager
from models import Aritcle

manager = Manager(app)

# @manager.command
# def runserver():
#     print('服务器跑起来了！')
#
# manager.add_command('db', DBmanager)

#1.要使用flask_migrate，必须绑定app,db
migrate = Migrate(app, db)
#2.把MigrateCommand命令添加到青奥manager里
manager.add_command('db', MigrateCommand)

if  __name__ == '__main__':
    manager.run()