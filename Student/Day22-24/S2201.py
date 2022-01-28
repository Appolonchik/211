#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_fun(*args, **kwargs):
    print(f'x = {args}, kwargs = {kwargs}')
    return True

my_fun(11, 3, 'Ольга', [1, 2, 3, 4, 5], {2}, 33, y=22)
my_fun(y = 11)
my_fun(3, y = 55, w=343)

w = [11,22,33,44,55,66,77,88,99]
tt = {'sep' : '<->', 'end' : 'QQQ\nqqq\n'}


print(w[0], w[1], w[2], w[3], w[4], sep ='<->', end='QQQ\nqqq\n')
print(*w, **tt)
print(*range(2, 122, 15))


print('END')
