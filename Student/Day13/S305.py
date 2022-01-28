#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

a, b, n = randint(20, 40), randint(20, 40), 1

while (ans := int(input(f'Сколько будет {a}*{b}: '))) != a * b:
    if a * b > ans:
        print(f' Ошибка {n}. Верный ответ больше')
    elif a * b < ans:
        print(f' Ошибка {n}. Верный ответ меньше')
    n += 1

print(f'Поздравляю! Ответ верный с {n} попытки!')
print('END')
