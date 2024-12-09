"""
@Time  :  2024/12/9 15:04
@Author:  Ryan
"""
from flask import Flask
from internal.router import Router


class Http(Flask):
    """Http服务引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
