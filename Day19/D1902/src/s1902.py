#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import join, abspath

data_path = join('..', 'data', 'elochka.txt')
print(data_path)
data_path = abspath(data_path)
print(data_path)

with open(data_path, mode='rt', encoding= 'utf-8') as src:
    for line in src:
        line = line.strip()
        print(line)



print('END')
