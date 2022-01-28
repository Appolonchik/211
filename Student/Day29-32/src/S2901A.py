# Программа для чтения и анализа файла json, построения графа
# и сохранения информации на диск с помощью модулей pickle и sqlite

import json
# import codecs
import pickle
import sqlite3
import os
from os.path import join, abspath


# Функция для совместного отображения названия станции и названия линии
def station_name(id_st):
    try:
        st_text = stations[id_st]["name"]
    except KeyError:
        st_text = f"<<< {id_st} >>>"
    try:
        lin_text = lines[stations[id_st]["line_id"]]["name"]
    except KeyError:
        lin_text = f"???????"
    result = st_text + " (" + lin_text + ")"
    return result


jpath = abspath(join("..", "Data", "scheme.json"))
print(jpath)

# Открываем файл json на чтение и весь его перегружаем в переменную schema
# with codecs.open(jpath, "r", "UTF-8") as src: # еще можно открыть файл так. Посмотреть, зачем модуль codecs!!!
with open(jpath, "rt", encoding="UTF-8") as src:
    # schema = json.loads(src.read())  # этот вариант для строк
    schema = json.load(src)            # этот вариант для файла

# Создаем пустой словарь для линий и наполняем его информацией о линиях из переменной schema
lines = {}
for m in schema["data"]["lines"]:
    lines[m["id"]] = {
        "id": m["id"],
        "name": m["name"]["ru"],
        "ordering": m["ordering"],
        "color": m["color"],
    }

# Создаем пустой словарь для станций и наполняем его информацией о станциях из переменной schema
stations = {}
for m in schema["data"]["stations"]:
    stations[m["id"]] = {
        "id": m["id"],
        "name": m["name"]["ru"],
        "ordering": m["ordering"],
        "line_id": m["lineId"],
        "perspective": m["perspective"],
        "color": lines[m["lineId"]]["color"],
    }

# Создаем пустой словарь для станций и наполняем его информацией о переходах из переменной schema
transitions = {}
for m in schema["data"]["transitions"]:
    transitions[m["id"]] = {
        "id": m["id"],
        "from_id": m["stationFromId"],
        "to_id": m["stationToId"],
        "perspective": m["perspective"],
        "bi": m["bi"],
        "length": m["pathLength"],
    }

# Создаем пустой словарь для станций и наполняем его информацией о пересадках из переменной schema
connections = {}
for m in schema["data"]["connections"]:
    connections[m["id"]] = {
        "id": m["id"],
        "from_id": m["stationFromId"],
        "to_id": m["stationToId"],
        "length": m["pathLength"],
        "perspective": m["perspective"],
        "bi": m["bi"]
    }

# Создаем граф
gr = {}

# Вносим данные о станциях
for key in stations:
    gr[key] = {"name": station_name(key)}

# Вносим данные о переходах
for val in transitions.values():
    id1, id2, ln12 = val["from_id"], val["to_id"], val["length"]
    pers, bi = val["perspective"], val["bi"]
    if(id1 in gr) and (id2 in gr) and (not pers) and bi:
        gr[id1][id2] = ln12
        gr[id2][id1] = ln12

# Вносим данные о пересадках
for val in connections.values():
    id1, id2, ln12 = val["from_id"], val["to_id"], val["length"]
    pers, bi = val["perspective"], val["bi"]
    # Если обе станции (по номерам id) существуют, построены и не являются перспективными
    if(id1 in gr) and (id2 in gr) and (not pers) and bi:
        gr[id1][id2] = ln12
        gr[id2][id1] = ln12

print("Все данные по станциям получены.")

# Задаем путь для сохранения файла pickle
data_path = abspath(join("..", "Data", "scheme.pickle"))
print(data_path)

# Открываем файл pickle обязательно в бинарном виде
with open(data_path, "wb") as dst:
    pickle.dump(gr, dst)
    pickle.dump(lines, dst)
    pickle.dump(stations, dst)
print(f"Все данные сохранены в {data_path} файл.")

# Задаем путь для сохранения файла sqlite3
base_path = abspath(join("..", "Data", "scheme.sqlite3"))
print(base_path)

# Удаляем файл базы данных, если он существует
try:
    os.remove(base_path)
except FileNotFoundError:
    pass

# Подключаемся к базе данных (создаем пустой файл базы данных)
con = sqlite3.connect(base_path)
cur = con.cursor()

# Формируем запрос для создания структуры базы данных
sql = """
CREATE TABLE gr(
    stn_id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE stn12_time(
    stn12_id INTEGER PRIMARY KEY,
    stn1 INTEGER,
    stn2 INTEGER,
    timen INTEGER
);
CREATE TABLE lines(
    line_id INTEGER PRIMARY KEY,
    color TEXT,
    id INTEGER,
    name TEXT,
    ordering INTEGER
);
CREATE TABLE stations(
    stations_id INTEGER PRIMARY KEY,
    color TEXT,
    id INTEGER,
    line_id INTEGER,
    name TEXT,
    ordering INTEGER,
    perspective INTEGER
);
"""

# Формируем структуру базы данных на основании запроса
try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print(f"Ошибка № 1: {err}")
else:
    print(f"База данных {base_path} успешно создана.")

# Подготавливаем данные для помещения в базу данных
try:
    # Таблица gr
    for x in gr:
        sdata = x, gr[x]["name"]
        sql = "INSERT INTO gr (stn_id, name) VALUES (?, ?)"
        cur.execute(sql, sdata)

     # Таблица stn12_time
    for x1 in gr:
        for x2 in gr[x1]:
            try:
                _ = int(x2)
                sdata = x1, x2, gr[x1][x2]
                sql = "INSERT INTO stn12_time (stn1, stn2, timen) VALUES (?, ?, ?)"
                cur.execute(sql, sdata)
            except ValueError:
                continue

     # Таблица lines
    for x in lines:
        sdata = (
            x,
            lines[x]["color"],
            lines[x]["id"],
            lines[x]["name"],
            lines[x]["ordering"],
        )
        sql = """INSERT INTO lines (line_id, color, id, name, ordering)
                VALUES (?, ?, ?, ?, ?)"""
        cur.execute(sql, sdata)

     # Таблица stations
    for x in stations:
        sdata = (
            x,
            stations[x]["color"],
            stations[x]["id"],
            stations[x]["line_id"],
            stations[x]["name"],
            stations[x]["ordering"],
            stations[x]["perspective"],
        )
        sql = """INSERT INTO stations (stations_id, color, id, 
                line_id, name, ordering, perspective)
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cur.execute(sql, sdata)

except sqlite3.DatabaseError as err:
    print(f"Ошибка № 2: {err}")
else:
    con.commit()  # Непосредственно запись в базу
    print(f"Все запросы добавления данных в базу успешно выполнены.")
con.close()

# Проверка отображения названий станций
# print(station_name(44))
# print(station_name(176))
# print(station_name(313))
# print(station_name(515))

# Проверка наличия и отображения названий всех станций по их id
# for n in range(550):
#     print(f"n = {n} --> {station_name(n)}")


print("END")
