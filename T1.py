# coding=utf-8

def fact(n):
    if(n==1):
        return 1;
    else:
        return n*fact(n-1);

def fact_filter(num, product):
    if num == 1:
        return product;
    return fact_filter(num-1, num*product);


def move(n ,a, b, c):
    if n==1:
        print(a, '---', c);
    else:
        move(n-1, a, c, b);
        move(1, a, b, c);
        move(n-1, b, a, c);
#print(move(3, 'A', 'B', 'C'));
#print(range(10))
