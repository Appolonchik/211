#!usr/bin/env/python3
# -*- coding: utf-8 -*-
from random import randint
from time import process_time

def bub_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

def nask(*, amin = 20, amax = 1_000):
    # Проверка входных параметров
    # Минимальное значение может быть только больше 20
    if amin < 20:
        amin = 20
    # Максимальное значение ограничено 1000
    if amax > 1_000:
        amax = 1_000
    # Запрос числа у пользователя
    # Запускаем бесконечный цикл
    while True:
        a = input(f'Введите целое число от {amin} до {amax} включительно: ')
        # Если пользователь ввел пустую строку, значит он ожидает максимальное число
        if not a.strip():
            a = amax
        #Начало обработки возможных ошибок ввода
        try:
            #Этот оператор может вызвать ошибку, если ввели текст
            a = int(a)
            # Сообщение пользователю о превышении мин и макс
            if a < amin:
                print(f'Введите число больше {amin}. Вы ввели {a}')
            elif a > amax:
                print(f'Введите число меньше {amax}. Вы ввели {a}')
            # Если число лежит в нижних границах, прерывание бесконечного цикла
            else:
                break
        # Сюда попадаем если оператор a = int(a) вызвал огибку ValueError
        except ValueError:
            # Вывод сообщения пользователю
            print(f'Повторите ввод. Вы ввели {a} - не является целым числом.')
        # Выполняем цикл еще раз
    return a


a = nask(amin=20, amax=1_000)
s1 = [randint(10_000, 99_999) for _ in range(a)]

print('\nПрограмма приступила к сортировке:')
t0 = process_time()
bub_sort(s1)
t1 = process_time() - t0

print(f'\nКолличество чисел в списке:        {len(s1):15}')

print(f'\nПроцессорное время сортировки:        {t1:8.3f} сек.')
print(f'\nСумма 10 минимальных чисел равна:  {sum(s1[:10]):15}')
print(f'\nСумма 10 максимальных чисел равна: {sum(s1[-10:]):15}')


print('END')
