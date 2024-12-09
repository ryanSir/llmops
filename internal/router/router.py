"""
@Time  :  2024/12/9 14:46
@Author:  Ryan
"""
from dataclasses import dataclass
from injector import inject
from flask import Flask, Blueprint
from internal.handler import AppHandler


@inject
@dataclass  # 当构造函数的参数很多的时候，可以使用此注解，隐藏构造函数
class Router:
    """路由"""
    app_handler: AppHandler  # 这里是实例而不是类，类的写法是app_handler = AppHandler

    # 依赖注释需要声明构造函数,如果想要不想声明，可以使用dataclass
    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1. 创建一个蓝图(可以看做是一组路由的集合，通过蓝图来管理路由)
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url与对应的控制器方法做绑定
        # app_handler = AppHandler()  此处注释掉，通过inject自动注入
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)  # GET 可省略
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)

        # 3. 在应用上去注册蓝图
        app.register_blueprint(bp)
