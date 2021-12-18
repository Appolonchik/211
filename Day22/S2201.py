#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_fun(*x, **y):
    print(f'x = {x}, y = {y}')
    return True

my_fun(11, 3, 'Ольга', [1, 2, 3, 4, 5], {2}, 33, y=22)
my_fun(y = 11)
my_fun(3, y = 55, Максим = 5, Дмитрий = 'Два')
my_fun(7, 11)
my_fun()
my_fun(111, y=222)

print('END', 4, 4, 6, 34, 5, 3, 5, 3, '<--->')
print('END', 4, 4, 6, 34, 5, 3, 5, 3, sep='<--->')
