#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from os import system, name

def clear():
	_ = system('clear')
import random
liczba = random.randint(1,49)
#print("Wylosowana liczba: ", liczba)

for i in range(6):
	print("Próba: ", i+1)
	odp = input("Jaką liczbę od 1 do 49 wylosowano? ")
	
	if liczba == int(odp):
		print("Hura!")
		break
	else:
		print("No niestety!")
		clear()
