#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввод чисел
def input_data():
    numbers = []
    while x := input("Введите числа: ").split():
        numbers += x
    return numbers

# Обработать данные
def comput_res(num):
    num = perevod(num)
    koln, minn, maxn = len(num),min(num),max(num)
    avrn = sum(num) / len(num)
    medn = sorted(num)[len(num)//2]
    return minn, maxn, avrn, medn, koln

def perevod(spis):
    temp_spis = []
    for x in spis:
        temp_spis.append(float(x))
    return temp_spis

# Вывод результата
def output_res(my_rez):
    minn, maxn, avrn, medn, koln = my_rez
    print(f' Всего введено числе {koln}')
    print(f' Минимум: {minn:12.4f}, Максимум: {maxn:2.4f}')
    print(f' Среднее: {avrn:12.4f}, Медиана: {medn:12.4f}')

my_numb = input_data()
our_res = comput_res(my_numb)
output_res(our_res)

print('END')
