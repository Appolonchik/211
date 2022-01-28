#!usr/bin/env/python3
# -*- coding: utf-8 -*-

def nfib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(f'1. Cоздание списка из 20 чисел Фибоначчи с помощью функции list():\n')
test1 = list(nfib(20))
print(test1)

print(f'\n\n2. Создание списка из 20 чисел Фибоначчи с помощью генератора списка:\n')
test2 = [x for x in nfib(20)]
print(test2)

print(f'\n\n3. Создание списка из 20 чисел Фибоначчи с помощью цикла for:\n')
for x in nfib(20):
    print(x, sep='', end=' ')

print(f'\n\n4. Cоздание множества из 20 чисел Фибоначчи с помощью генератора множества:\n')
test3 = {x for x in nfib(20)}
print(f'{test3}\n')



print('END')
