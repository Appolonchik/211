#!/usr/bin/env python3
# -*- coding: utf-8 -*-

txt = '''Пользователь вводит текст, состо€щие из
нескольких слов. Выведите слово, которое в
этом тексте встречается чаще всего и длина
которого больше трех символов регистр не учитываем
если таких слов несколько, выведите то,
последние три символа слова меньше всего.
Стоящие практика стоящие практика стоящие практика'''

line = txt.lower().split()
counter = {}
def gen3(s):
    for x in s:
        if len(x) > 3:
            yield x

for word in line:
    if word in counter:
        counter[word] = counter[word] + 1
    else:
        counter[word] = 1
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]

print(counter)
print(most_frequent)

print(f' Наиболее частое слово {min(most_frequent)} встречается'
    f' {max_count} раза')

print('END')
