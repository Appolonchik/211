#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def new_my_fun(*args, **kwargs):
    print('Внимание! Работает новая функция!')
    print(f'x_new = {args}, kwargs_new = {kwargs}')
    print('Новая функция завершила работу!')
    return True


def my_fun(*args, **kwargs):
    print(f'x = {args}, kwargs = {kwargs}')
    new_my_fun(*args, **kwargs)
    print('*' * 50, '\n')
    return True

my_fun(y=22)
my_fun(y=11)
my_fun(3, 12, 33, 55, 5675, 441, y=55, w=343)

tt = {'sep': '<->', 'end': 'QQQ\nqqq\n'}
w = [11, 22, 33, 44, 55]


print('END')