#coding=utf-8
import os;
path = "C:\\Users\\Administrator\\Desktop\\a.txt"

with open(path, 'a+', encoding='gbk') as f:
    s = f.write("\n这是第aa11234行，this is four line");
    print(s);
