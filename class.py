# coding = utf-8
from wx import Frame
class Sup(object):
    sex = "man"
    def __init__(self):
        self.name = 123
        print("实例化开始后就执行__init__")
class sub(Frame,Sup):
    def __init__(self):

        print(Sup().name)
sub()

