#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# S2202.py
#
from skvek import Vektor

a = Vektor(x=2.8, y=8)
b = Vektor(alfa=51, r=12)
a.output()
b.output()

h = a.x
print(f'{a.x=}')
print(f'{a.y=}')
print(f'{a.r=}')
print(f'{a.alfa=}')


print('END')
