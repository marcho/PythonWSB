import random
slowa = ("python","gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
#print(word)
poprawnie = word
pomie =""
while word:
	position = random.randrange(len(word))
	pomie += word[position]
	word = word[:position] + word[(position + 1):]
print (pomie)
punkty = 5
print("""Witaj w grze 'Wymieszane litery'! Uporządkuj litery, aby odtworzyć prawidłowe słowo. (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)""")
print("Maksymalnie w grze można zdobyć {} punktów. Za każdą udzieloną podpowiedź, tracimy 1 punkt.".format(punkty))
print ("Zgadnij, jakie to słowo:", pomie)
zgaduj = input("\nTwoja odpowiedź: ")
liczba_szans_do_podpowiedzi = 3
while zgaduj != poprawnie and zgaduj != "":
	print ("Niestety, to nie to słowo.")
	zgaduj = input("Twoja odpowiedź: ")
	liczba_szans_do_podpowiedzi -= 1
	if liczba_szans_do_podpowiedzi < 0:
		pomoc = input("Czy potrzebujesz podpowiedź? Wpisz t jeśli tak. ")
		if pomoc == "t":
			punkty -= 1
			if poprawnie == "python":
				print("Właśnie programujesz w tym języku.")
				zgaduj = input("Twoja odpowiedź: ")
			if poprawnie == "gdansk":
				print("Miasto sąsiedzkie do Gdyni, znajduje się tam drugi oddział WSB.")
				zgaduj = input("Twoja odpowiedź: ")
			if poprawnie == "dlaczego":
				print("Tym słowem zaczynasz zdanie, kiedy pytasz kogoś o powód zrobienia czegoś.")
				zgaduj = input("Twoja odpowiedź: ")
			if poprawnie == "gdynia":
				print("Jesteś w tym mieście")
				zgaduj = input("Twoja odpowiedź: ")
			if poprawnie == "wsb":
				print("Twoja obecna uczelnia")
				zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
	print("Zgadza się! Zgadłeś!\n")
	print("Zdobyłeś {} punktów".format(punkty))
print("Dziękuję za udział w grze.")
