"""
@Time  :  2024/12/9 14:31
@Author:  Ryan
"""
from injector import Injector, inject


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A 的 name: {self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
