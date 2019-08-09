# -*- coding: utf-8 -*-
# 蓝本中的错误处理程序
from flask import render_template
from . import main


# 如果使用 errorhandler 修饰器，那么只有蓝本中的
# 错误才能触发处理程序。要想注册程序全局的错误处理程序，必须使用 app_errorhandler
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@main.errorhandler(401)
def page_not_found(e):
    return render_template('401.html'), 401

@main.errorhandler(403)
def page_not_found(e):
    return render_template('upError.html'), 403