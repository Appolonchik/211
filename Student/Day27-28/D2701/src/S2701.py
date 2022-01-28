#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1600
from pprint import pprint
from copy import deepcopy
from time import process_time
from os.path import join, abspath
import sys

def solve(sudo):
    sol = [[y for y in x] for x in sudo]
    if solstep(sol):
        return sol

def solstep(sol):
    while True:
        min_pos = None
        for ri in range(9):
            for ci in range(9):
                if sol[ri][ci]:
                    continue
                pv = gpv(ri, ci, sol)
                pv_count = len(pv)
                if not pv_count:
                    return False
                if pv_count == 1:
                    sol[ri][ci], = pv # - красивый вариант
                    #sol[ri][ci] = next(iter(pv)) - стандартный вариант
                    #sol[ri][ci] = list(pv)[0]
                if not min_pos or pv_count < len(min_pos[1]):
                    min_pos = (ri, ci), pv
        if not min_pos:
            return True
        elif len(min_pos[1]) >= 2:
            break
    (r, c), z = min_pos # Начало ветвления
    for v in z:
        # sol_copy = [[y for y in x] for x in sol]
        sol_copy = deepcopy(sol)
        sol_copy[r][c] = v
        if solstep(sol_copy):
            for r in range(9):
                for c in range(9):
                    sol[r][c] = sol_copy[r][c]
            return True
    # return False - Можно не писать она все равно выведет None

def grv(ri, sudo):
    return set(sudo[ri])

def gcv(ci, sudo):
    return {line[ci] for line in sudo} # оптимальный вариант
    #res = set() - Первый вариант самый простой
    #for line in sudo:
        #res.add(line[ci])
    #return res
    #return set(line[ci] for line in sudo) - второй вариант
    
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

def pr_sudok(s, dst=sys.stdout):
    print('+-------+-------+-------+', file=dst)
    for k in range(9):
        print('|', s[k][0], s[k][1], s[k][2], '|',
                   s[k][3], s[k][4], s[k][5], '|',
                   s[k][6], s[k][7], s[k][8], '|', file=dst)
        if k%3 == 2:
            print('+-------+-------+-------+', file=dst)
    
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

sudo = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
    
]

def convsud(strsud):  # вариант Александрова
    sudo = [[int(strsud[x * 9 + y]) for y in range(9)] for x in range(9)]
    return sudo


def convsud_4(strsud):  # вариант Ксенофонтова
    sudo = [[int(i) for i in strsud[j:j+9]] for j in range(0, 81, 9)]
    return sudo


def convsud_5(strsud):  # вариант Урдина
    sudo = [[*map(int, strsud[i: i + 9])] for i in range(0, 81, 9)]
    return sudo


def convsud_6(strsud):  # вариант Рулёва (по 5му)
    sudo = [list(map(int, strsud[i: i + 9])) for i in range(0, 81, 9)]
    return sudo


def convsud_7(strsud):  # вариант Жабко
    sudo = []
    for k in range(0, 81, 9):
        row = [l for l in strsud[k: k+9]]
        stk = list(map(int, row))
        sudo.append(stk)
    return sudo


def convsud_8(strsud):  # вариант Рулёва (по 7му)
    sudo = []
    for k in range(0, 81, 9):
        stk = list(map(int, strsud[k: k+9]))
        sudo.append(stk)
    return sudo


def convsud_9(strsud):  # вариант Рулёва
    sudo = [[list(map(int, strsud))[i * 9 + j] for j in range(9)]
            for i in range(9)]
    return sudo


def convsud_10(strsud):  # вариант Maxim'а (аналогичный 8му)
    a = list(map(int, strsud[0:9]))
    b = list(map(int, strsud[9:18]))
    c = list(map(int, strsud[18:27]))
    d = list(map(int, strsud[27:36]))
    e = list(map(int, strsud[36:45]))
    f = list(map(int, strsud[45:54]))
    g = list(map(int, strsud[54:63]))
    h = list(map(int, strsud[63:72]))
    i = list(map(int, strsud[72:81]))
    sudo = [a, b, c, d, e, f, g, h, i]
    return sudo


tpath = join('..', 'Data', 'sudoky100.txt')
tpath = abspath(tpath)
print(tpath)

spath = join('..', 'Data', 'sudoky_solved.txt')
spath = abspath(spath)
print(spath)


with open(spath, 'wt', encoding='UTF-8') as dst, \
     open(tpath, 'rt', encoding='UTF-8') as src:
    n = 0
    tall0 = process_time()
    for line in src:
        line = line.strip()
        if len(line) == 81:
            # print(line)
            n += 1
            sudolist = convsud(line)
            pr_sudok(sudolist, dst=dst)
                
            t0 = process_time()
            res = solve(sudolist)
            t = process_time() - t0
                
            if res:
                pr_sudok(res, dst=dst)
                print(f'Судоку {n:3} решена за {t} сек.')
                print(f'Судоку {n:3} решена за {t} сек.\n', file=dst)
            else:
                print(f'Судоку {n:3} не решена за {t} сек.')
                print(f'Судоку {n:3} не решена за {t} сек.\n', file=dst)
    tall = process_time() - tall0
    print(f'\n\nВсе {n} судоку решены за {tall} сек.')
    print(f'\n\nВсе {n} судоку решены за {tall} сек.', file=dst)
    

print('END')
