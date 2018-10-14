import random
slowa = ("python","gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
poprawnie = word
#print (poprawnie)
liczba_liter = word.count('')
liczba_liter -= 1
print("Zostało wylosowane dla Ciebie słowo, mające {} liter.".format(liczba_liter))
print ("Musisz odgadywać słowo, odkrywając jedną literkę na raz")
liczba_szans = 5
while liczba_szans > 0:
	zgaduj = input("\nTwoja odpowiedź: ")
	if word.count(zgaduj) > 0:
		print("Tak, Twoja litera znajduje się w wyrazie")
	else:
		print("Niestety, tej litery nie ma w wyrazie")
	liczba_szans -= 1
	print("Pozostało szans: {}".format(liczba_szans))
print("Została Twoja ostatnia szansa, spróbuj zgadnąć wyraz.")
zgaduj = input("\nTwoja odpowiedź: ")
if zgaduj == poprawnie:
	print("Zgadłeś!")
else:
	print("Niestety, nie zgadłeś. Poprawna odpowiedź to {}.".format(poprawnie))
print("Dziękuję za udział w grze.")
