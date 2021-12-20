#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# S2202.py
#
from skvek import Vektor

a = Vektor(x=2.8, y=8)
b = Vektor(alfa=51, r=12)
a.output()
b.output()
a.alfa = 45
a.output()

print(a)
print(f'{b=}')


print('END')
