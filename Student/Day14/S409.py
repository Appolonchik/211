#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Используйте срезы в замечательном языке Python!!!'
print(f'>{s}<')
print(f'>{s[2]}<')
print(f'>{s[-4]}<')
print(f'>{s[:5]}<')
print(f'>{s[:-3]}<')
print(f'>{s[::2]}<')
print(f'>{s[1::2]}<')
print(f'>{s[::-1]}<')
print(f'>{s[-4:9:-1]}<')
print(f'>{s[10:-3]}<')
print(f'>{len(s)}<')
print(f'>{len(s.split())}<')
print(*s.split()[::-1])
print(f'>{" ".join(s.split()[::-1])}<')

print('END')
