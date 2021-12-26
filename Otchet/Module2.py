#!usr/bin/env/python3
# -*- coding: utf-8 -*-

txt = """Анализ текста по буквам. Практическое задание №2

Написать программу на Python для анализа данного текста, который сохранён в переменной txt по буквам. Программа на Python должна проанализировать данный текст и вывести, или, как некоторые Users говорят, напечатать следующую информацию. Необходимо вывести:

# Общее количество букв в данном тексте
# Общее количество слов в данном тексте. Словом, считаются любые символы, разделённые пробелами или переходом на следующую строку.
# Подсчитать, каких букв и сколько встречается в тексте
# Вывести их на печать
# 1) в алфавитном порядке
# 2) в порядке убывания частоты
# Регистр букв значения не имеет! Например, в тексте 'Aa' буква 'а'
# встречается 2 раза
# В структуре данных, которую вы выберете для хранения информации
# во время работы программы, НЕ ХРАНИТЬ буквы, которые не встретились"""

# ***********************************
# Тут должна находиться Ваша программа
def word_caclculate(spis_line):
    n_letters = 0
    for lin in spis_line:
        lin = lin.strip()
        n_letters += len(lin)
    return  n_letters

s1="".join(c for c in txt if c.isalpha())
nl = word_caclculate(s1)
print(f'\nВ тексте txt - {nl} буквы')

print(f'\nВ тексте txt - {len(txt.split())} слов')

s1 = s1.lower()
dsimbols = {}
    
for letter in s1:
    if letter in dsimbols:
        dsimbols[letter] += 1
    else:
        dsimbols[letter] = 1

list_simbols1 = list(dsimbols.items())
list_simbols1.sort()

list_simbols2 = [(n,l) for l, n in dsimbols.items()]
list_simbols2.sort(reverse=True)

print('\nБуквы в тексте в алфавитном порядке:')
print('*' * 50)
for b, n in list_simbols1:
    print(f'Буква {b} встречается в тексте {n:3} раз.')

print('\nБуквы в порядке убывания частоты:')
print('*' * 50)
for n, b in list_simbols2:
    print(f'Буква {b} встречается в тексте {n:3} раз.')

print('*' * 50)

print('\nEND')
