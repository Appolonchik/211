#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит строку из нескольких слов.
Выведите све слова с четными индексами:
>Пользователь строку нескольких '''

a = input(':>').split()[::2]

txt = ''
for word in a:
    txt += word + ' '

s = ' '.join(a)

print(f'>{a}<')
print(*a)
print(txt)
print(s)

print('END')
