# -*- coding:utf-8 -*-
# 此文件的作用：一是包含应用工厂；二是 告诉 Python flaskr 文件夹应当视作为一个包。

import os
from flask import Flask


# 应用工厂函数
def create_app(test_config=None):
    # 创建 Flask 实例
    # 实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统
    app = Flask(__name__, instance_relative_config=True)
    # 设置一个应用的 缺省配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # 使用 config.py 中的值来重载缺省配置
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 代实例配置，可以实现 测试和开发的配置分离，相互独立
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

