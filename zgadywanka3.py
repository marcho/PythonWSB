#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random
listaLiczb = []
ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną liczbę: "))
print("Wytypuj", ileliczb, " z ", maksliczba, "liczb: ")

for i in range(0, ileliczb):
	listaLiczb.append(random.randint(0,maksliczba))

print (listaLiczb)


for i in range(6):
	print("Próba: ", i+1)
	zgadywanaLiczba = input("Podaj liczbę: ")
	if int(zgadywanaLiczba) in listaLiczb:
		print("Zgadłeś!")
		break
	else:
		print("Nie zgadłeś!")
