#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input(' Введите количество минут с начала любых суток: '))

n = n % (24*60)
h = n // 60
m = n % 60


print(f'С начала последних суток прошло {h} часов и {m} минут.')

print('END')