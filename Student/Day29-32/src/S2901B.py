#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import join, abspath
import pickle
from prettytable import PrettyTable
from S2901A import station_name

#def station_name(id_st):
    #try:
        #st_text = stations[id_st]['name']
    #except KeyError:
        #st_text = f'<<< {id_st} >>>'
        
    #try:
        #lin_text = lines[stations[id_st]['line_id']]['name']
    #except KeyError:
        #lin_text = '??????????'
    #result = st_text + ' (' + lin_text + ')'
    #return result



# Организация диалога с пользователем
#nach_kon = 'начальн'


def spros(nach_kon):
    # Создаем словарь для установления соответствия между порядковым номером,
    # который будет вводить пользователь, и номером линии в нашей базе
    templn = {}
    # Выводим список порядковых номеров и названий станций
    myTable = PrettyTable(["№ линии", "Название линии"])
    for (no, nl, line_name), nr in zip(temp_lines, range(1, 100)):
        templn[nr] = nl
        myTable.add_row([nr, line_name])
    # print(f"{nr:2}  {line_name}") # вместо этого сделали Prettytable
    print(myTable)

    nline = int(input(f"\nВведите номер линии {nach_kon}ой станции: "))
    nline = templn[nline]
    print(f"Выбрана {nach_kon}ая линия: {lines[nline]['name']}\n")

    # Создаем словарь для установления соответствия между порядковым номером,
    # который будет вводить пользователь, и номером станции в нашей базе
    tempst = {}
    n = 0
    myTable = PrettyTable(["№ станции", "Название станции", "Id_st"])
    for sta in stations.values():
        if sta["line_id"] == nline:
            n += 1
            myTable.add_row([n, station_name(sta["id"]), sta["id"]])
            tempst[n] = sta["id"]
    myTable.align["Название станции"] = "l"
    print(myTable)

    nst = int(input(f"Введите номер {nach_kon}ой станции: "))
    nst1 = tempst[nst]
    # print(f"Выбрана {nach_kon}ая станция: {station_name(nst1)} {nst1}")
    return nst1
# ****************************************

def findminp(nst2, nst1):
    u, s, p = set(), {nst1: 0}, {}
    while True:
        n, m = None, None
        for x in s:
            if x not in u:
                if n  == None:
                    n, m = x, s[x]
                else:
                    if s[x] < m:
                        n, m = x, s[x]
        if n == None:
            return None
        if n == nst2:
            result = [nst2]
            # приехали
            x = nst2
            while x != nst1:
                x = p[x]
                result.append(x)
            return result, s[nst2]
        u.add(n)
        for x in gr[n]:
            try:
                _ = int(x)
            except ValueError:
                continue
            if x not in u:
                if x not in s:
                    s[x], p[x] = gr[n][x] + m, n
                else:
                    if s[x] > gr[n][x] + m:
                        s[x], p[x] = gr[n][x] + m, n 

data_path = abspath(join('..', 'Data', 'scheme.pickle'))
with open(data_path, mode='rb') as dst:
    gr = pickle.load(dst)
    lines = pickle.load(dst)
    stations = pickle.load(dst)
print(f'Все данные из {data_path} по станциям и линиям восстановлены')

temp_lines = [(x['ordering'], x['id'], x['name']) for x in lines.values()]
temp_lines.sort()

nst1 = spros('начальн')
# print(nst1)

nst2 = spros('конечн')
# print(nst2)

print(f'\nВыбрана начальная станция: {station_name(nst1)} {nst1}')
print(f'Выбрана конечная станция: {station_name(nst2)} {nst2}')

print(f'Ищем минимальный путь между {nst1} и {nst2}')
# nst1, nst2 = nst2, nst1
res = findminp(nst1, nst2)
# print(res)
if res:
    myTable = PrettyTable(['Время', 'Название станции', 'Id_st'])
    mpas, minp = res
    xold = None
    tx = 0
    for x in mpas:
        if xold:
            tx += gr[xold][x]
        else:
            tx = 0
        myTable.add_row([
            f'{tx//3600:02d}:{(tx%3600)//60:02d}:{tx%60:02d}',
            f'Станция {station_name(x)}',
            f'({x})'
        ])
        xold = x
    myTable.align['Название станции'] = 'r'
    print(myTable)
    print(
        f'Общее время пути: {tx//3600:02d} час.'
        f':{(tx%3600)//60:02d} мин. и :{tx%60:02d} сек.'
    )
    
else:
    print('Путь между станциями не найден.')


print('END')
