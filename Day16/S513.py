#!/usr/bin/env python3
# -*- coding: utf-8 -*-

txt = '''Пользователь вводит текст состо€щие из
нескольких слов Выведите слово которое в
этом регистр тексте встречается чаще всего и длина
которого больше трех символов регистр не учитываем
если таких слов несколько выведите то всего РЕГИСТР
последние три символа слов меньше всего выведите
Стоящие прАктика стоЯщие праКтика стОящие Практика'''

line = txt.lower().split()
counter = {}
def gen3(s):
    for x in s:
        if len(x) > 3:
            yield x

for word in gen3(line):
    if word in counter:
        counter[word] = counter[word] + 1
    else:
        counter[word] = 1
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
most_frequent = sorted(most_frequent, key=lambda x : x[-3:])

print(f'Наиболее частое слово - "{most_frequent[0]}" - встречается'
    f' {max_count} раза')

print('END')
