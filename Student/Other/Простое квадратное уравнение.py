#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
if a == 0:
    if b == 0:
        if c == 0:
            print('Корень - любое число')
        else:
            print('Нет корней')
    else:
        x = -c/b
        print('Один корень ' + str(x))
else:
    d = b*b - 4*a*c
    dkor = d**(0.5)
print(a,b,c)
print('END')