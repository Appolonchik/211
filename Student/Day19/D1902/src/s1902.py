#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import join, abspath

data_path = join('..', 'data', 'elochka.txt')
print(data_path)
data_path = abspath(data_path)
print(data_path)

write_path = join('..', 'data', 'new_elochka.txt')
print(write_path)
write_path = abspath(write_path)
print(write_path)

with open(write_path, 'wt', encoding='utf-8') as dst:
    with open(data_path, encoding= 'utf-8', mode='rt') as src:
        n = 0
        for line in src:
            n += 1
            line = line.strip()
            print(f'{n:3} {len(line):3} {len(line.split()):2} {line}', file=dst)
            


print('END')
