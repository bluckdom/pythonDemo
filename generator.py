#coding=utf-8


def yhTriangle(n):
    l, index = [1], 0
    while index < n:
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        index += 1
for x in yhTriangle(3):
   print(x)