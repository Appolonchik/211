#!/usr/bin/env python3
# -*- coding: utf-8 -*-

k = {'Антон', 'Коля', 'Алена', 'Елена', 'Миша', 'Галя'}
ks = iter(k)

for x in k:
        print(f'{x}, сколько будет 2+2*2?')

while True:
    try:
        x = next(ks)
        print(f'{x}, сколько будет 2+2*2?')
    except StopIteration:
        break

print('END')
