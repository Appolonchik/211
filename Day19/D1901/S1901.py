#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def food_generator():
    yield "Сок"
    for dish in ['Салат', 'Снеки', 'Холодец', 'Картошка фри']:
        yield dish
    yield 'Супер Пайтон пица от шефа'
    for n in range(1, 4):
        yield 'Закурска № ' + str(n)
    yield 'Кофе'
    yield 'Пончик'
    yield 'Десерт'
    yield 'Счет клиенту'


cl_ivan = food_generator()
print(next(cl_ivan))
print(next(cl_ivan))
print(next(cl_ivan))
for x in cl_ivan:
    print(f'Подать блюдо {x}')

cl_olga = food_generator()
print(list(cl_olga))

print('END')
