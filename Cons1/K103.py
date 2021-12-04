#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')
'ru_RU'

t = datetime.now()
#t = datetime(2021, 11, 24, 13, 30)
nam = input('Введите Ваше имя: ')
h = t.hour

print(f'{t}, {h}')

if 7 <= h < 10:
    print(f'Доброе утро, {nam}!')
elif 10 <= h < 17:
    print(f'Добрый день, {nam}!')
elif 17 <= h < 23:
    print(f'Добрый вечер, {nam}!')
else:
    print(f'Доброй ночи, {nam}!')

# час - 1 21
# часов - 0 5-20
# часа - 2-4 22 23

if (not h) or (5 <= h <= 20):
    hours = "часов"
elif h == 1 or h == 21:
    hours = "час"
else:
   hours = "часа"

# минут 0 5-20  * 40 45-49
# минута 1 21   * 41
# минуты 2-4    * 42-44
# минут от 5 до 20

m = t.minute
if 5 <= m <= 20:
    minutes = "минут"
elif 2 <= m%10 <= 4:
    minutes = "минуты"
elif m%10 == 1:
    minutes = "минута"
else:
    minutes = "минут"

mon = ['Января','Февраля','Марта','Апреля','Мая','Июня',
    'Июля','Августа','Сентября','Октября','Ноября','Декабря']
nmon = mon[t.month-1]

print(f'Сегодня {t.day} {nmon} {t.year} года')
print(f'Текущее время {t.hour} {hours} {t.minute} {minutes}')

print('END')
