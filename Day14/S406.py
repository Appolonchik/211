#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит строку, состоящую
ровно из двух слов, разделенных одним пробелом.
Поменяйте эти слова местами и напечатайте их.
    Люблю Python    .
Для решения задачи не стоит строчку split'''

s = input('Введите два слова: ').strip()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]

s = second_word + ' ' + first_word

print(f'>{s}<')

print('END')
