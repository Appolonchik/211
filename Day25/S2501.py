#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Необходимо написать функцию генератора, реализующую вычисление
факториала и проверить ее работу с использованием функции list,
генератора списков, цикла for и генератора множеств.'''
# Факториал это произведение чисел от 1 до n. n! = 1*2*3*4=14
# 1, 2, 6, 24, 120, 720, и т.д.

from time import process_time


def faktor(n):
    f = 1
    for m in range(1, n + 1):
        f *= m
    return f

x = 10_000
t0 = process_time()
print(f' x = {x}     len(x!) = {len(str(faktor(x)))}')
t = process_time() - t0
print(f'Время работы программы составило {t} сек.')



print('END')
