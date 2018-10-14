#!/usr/bin/env python3
#-*- coding: utf-8 -*-

pierwsza = input("Podaj pierwszą liczbę ")
druga = input("Podaj drugą liczbę ")
co_ile = input("Podaj wielkość krodku ")

print('Liczenie od {} do {}'.format(pierwsza, druga))
for i in range(pierwsza, druga+1, co_ile):
	print (i)
