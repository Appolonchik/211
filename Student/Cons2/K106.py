#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввод чисел
def input_data():
    numbers = []
    x = None
    while x != []:
        x = input("Введите числа: ").strip().split()
        numbers += x
        print(f' >{x}<')

    #numbers = [15, 85, 86, 95, 2, 45, 19, 35, 85, 45, 85, 3, 54, 68, 23]
    return numbers

# Обработать данные
def comput_res(num):
    return 2, 95, 745/15, 45, 15

#  Вывод результата
def output_res(my_rez):
    minn, maxn, avrn, medn, koln = my_rez
    print(f' Всего введено числе {koln}')
    print(f' Минимум: {minn:8.4f}, максимум: {maxn:8.4f}')
    print(f' Среднее:  {avrn:8.4f},  медиана:   {medn:8.4f}')

my_numb = input_data()
our_res = comput_res(my_numb)
output_res(our_res)

print('END')
