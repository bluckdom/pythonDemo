# coding=utf-8

class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, slice):
            print("123123")
        if isinstance(item, int):
            print("int")
f = Fib()

f[0]