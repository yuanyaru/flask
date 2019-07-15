# -*- coding:utf-8 -*-

import os
from flask import Flask


# 应用工厂函数
def create_app(test_config=None):
    # 创建Flask实例
    # 实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统
    app = Flask(__name__, instance_relative_config=True)
    # 设置一个应用的 缺省配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    return app

