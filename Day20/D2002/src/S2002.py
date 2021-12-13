#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import join, abspath

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
        print(line)
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



print('END')
