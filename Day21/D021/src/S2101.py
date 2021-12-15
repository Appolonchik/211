#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Импортируем библиотеки для работы с путями 
from os.path import join, abspath
import sqlite3

base_path = join('..', 'Data', 'Learn.sqlite3')
base_path = abspath(base_path)
print(base_path)

course_path = abspath(join('../Data/course.txt'))
print(course_path)


with sqlite3.connect(base_path) as con:
    with open(course_path, mode='rt', encoding='cp1251') as src:
        try:
            cur = con.cursor()
            for line in src:
                line = line.strip()
                if line:
                    cnam, ccode, cdur = line.split(';')
                    sdata = cnam.strip(), ccode.strip(), int(cdur)
                    sql = '''INSERT INTO Course
                    (CourseName, CourseCode, CourseDuration) 
                    VALUES (?, ?, ?);'''
                    cur.execute(sql, sdata)
        except sqlite3.DatabaseError as err:
            print(f'Ошибка 1: {err}')
        else:
            con.commit()
            print(f'Все запросы добавлены в БД {base_path} выполнены')
                    



print('END')
