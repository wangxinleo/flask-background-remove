# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
sqlalchemy = SQLAlchemy()

def create_app(config_name):
    '''程序的工厂函数'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 将配置类中的配置导入程序
    config[config_name].init_app(app)

    # 初始化扩展
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    sqlalchemy.init_app(app)

    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
