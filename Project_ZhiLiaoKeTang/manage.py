#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoYu on 18-1-31

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlktqa import app
from exts import db
manager = Manager(app)

#绑定app db
migrate = Migrate(app, db)

#添加迁移脚本的命令到manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()