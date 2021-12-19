#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myvek.py
#
class Vektor(object):

    def __init__(self, *, x=None, y=None, alfa=None, r=None):
        print('Я создаю новый пакет молока', x,y,alfa,r)
        self.x = x
        self.y = y
        self.alfa = alfa
        self.r = r
