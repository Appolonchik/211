#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1600
from pprint import pprint

def grv(ri, sudo):
    return set(sudo[ri])

def gcv(ci, sudo):
    return {line[ci] for line in sudo} # оптимальный вариант
    #res = set() - Первый вариант самый простой
    #for line in sudo:
        #res.add(line[ci])
    #return res
    # return set(line[ci] for line in sudo) - второй вариант
    
def gbv(ri, ci, sudo):
    brs = 3 * (ri // 3)
    bcs = 3 * (ci // 3)
    return {sudo[brs + x][bcs + y]
            for x in range(3)
            for y in range(3)
            }

def gpv(ri, ci, sudo):
    res = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    res -= grv(ri, sudo)
    res -= gcv(ci, sudo)
    res -= gbv(ri, ci, sudo)
    return res
    

sudo = [
    [9, 5, 7, 8, 4, 3, 6, 1, 2],
    [4, 8, 3, 6, 2, 1, 7, 5, 9],
    [6, 2, 1, 5, 9, 7, 8, 3, 4],
    
    [1, 6, 8, 4, 3, 2, 9, 7, 5],
    [5, 4, 9, 1, 7, 6, 3, 2, 8],
    [3, 7, 2, 9, 8, 5, 1, 4, 6],
    
    [7, 3, 5, 2, 6, 9, 4, 8, 1],
    [2, 9, 4, 3, 1, 8, 5, 6, 7],
    [8, 1, 6, 7, 5, 4, 2, 9, 3],
    
]


sudo1 = [
    [0, 5, 0, 8, 0, 3, 0, 0, 0],
    [0, 8, 3, 6, 2, 0, 0, 0, 0],
    [6, 0, 1, 0, 0, 7, 8, 0, 4],
    
    [0, 6, 0, 0, 0, 0, 0, 7, 5],
    [5, 0, 9, 1, 0, 6, 3, 0, 8],
    [3, 7, 0, 0, 0, 0, 0, 4, 0],
    
    [7, 0, 5, 2, 0, 0, 4, 0, 1],
    [0, 0, 0, 0, 1, 8, 5, 6, 0],
    [0, 0, 0, 7, 0, 4, 0, 9, 0],
    
]

pprint(sudo)

for r in range(9):
    for c in range(9):
        if not sudo[r][c]:
            print(f' R={r+1} C={c+1} {gpv(r, c, sudo)}')

print('END')
