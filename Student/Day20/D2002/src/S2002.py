#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import join, abspath

def word_caclculate(spis_line):
    '''функция подсчитывает количество слов и букв в тексте
    который состоит из списка строк.'''
    # Задаем начальное количество
    #n_words, n_letters = 0, 0
    n_words = 0
    n_letters = 0
    # Делаем цикл по строкам в списке
    for lin in spis_line:
        # Удаляем начальные и конечные пробелы
        lin = lin.strip()
        # Увеличиваем количество символов
        n_letters += len(lin)
        # Увеличиваем число слов
        n_words += len(lin.split())
    # Возвращаем кортеж (скобки не нужны!): (количество_слов, количество_букв)
    return n_words, n_letters
    
    
data_path = join('..', 'Data', 'elochka.txt')
data_path = abspath(data_path)
print(data_path)

# Пустой словарь для слов. Способ №1
bslov = {}

# Пустой словарь для букв. Способ №2
dsimbols = dict()

# Открываем файл на счетния до конца блока with
# При выходе файл будет автоматически закрыт
# и становитяся недоступным
with open(data_path, mode='rt', encoding='utf-8') as src:
    # Считываю файл по строчкам через цикл в переменную line
    for line in src:
        # Перевожу в нижний регистр и удаляю внешние пробелы
        line = line.strip().lower()
        # Анализируем буквы
        for letter in line:
            if letter in dsimbols:
                # Если буква уже есть в нашем словаре
                # Прибавляем к старому значению 1
                dsimbols[letter] += 1
            else:
                # Если буквы еще нет в нашем словаре
                # Записываем значение 1 (первая буква попалась)
                dsimbols[letter] = 1
        # Анализируем слова
        for word in line.split():
            # ==============================================
            # Отберем слова в которых больше чем 2 символа #
            # ==============================================
            if len(word) > 2:
                # Добавляю их в словарь, увеличивая старое значение на 1
                # Метод get возвращает значение 0 (мы его указали) если слова нет!!!
                bslov[word] = bslov.get(word, 0) + 1

# В переменной song формируем текст песни в виде списка строк
with open(data_path, mode='rt', encoding='UTF-8') as src:
    song = list(src)

# Создаем список из кортежей (буква, количество)
list_simbols1 = list(dsimbols.items())
# Сортируем список по кортежу (реально по первому элементу кортежа)
list_simbols1.sort()

# Используя генераторы списков создаем список из кортежей (количество, буква)
list_simbols2 = [(n,l) for l, n in dsimbols.items()]
# Сортируем список по первому элементу кортежа - кол
list_simbols2.sort(reverse=True)

print('Буквы в тексте в алфавитном порядке:')
print('*' * 50)
for b, n in list_simbols1:
    print(f'Буква {b} встречается в тексте {n:3} раз.')

print('\n\nБуквы в тексте по частоте появления:')
print('*' * 50)
# Идет разбор кортежа №2. Символы n и b в обратном порядке!!!
for n, b in list_simbols2:
    print(f'Буква {b} встречается в тексте {n:3} раз.')

# Анализ слов в тексте
spis = [(n, l) for l, n in bslov.items()]
spis.sort(reverse=True)
print('\n\nСлова в тексте по частоте появления:')
print('-' * 50)
# Разбор кортежа символы n и b в обратном порядке!!!
for n, b in spis:
    print(f'Слово {b} встречается в тексте {n} раза.')

# Используем нашу функцию word_caclculate для подсчета количества слов и букв
nw, nl = word_caclculate(song)
print(f'\n\nВ песне {nw} слова и {nl} буквы.')

print('END')
