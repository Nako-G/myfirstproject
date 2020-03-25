ZADANIE 1

import random
x = random.randrange(1, 10)

print("Znajdź liczbę z przedziału od 1 do 10 w trzech ruchach i wygraj nagrodę!")
próba = 2
for próba in range(próba, -1, -1):
    liczba = int(input("Wpisz liczbę: "))
#    print("Pozostało {0} prób.".format(próba))

    if liczba < x:
        print("ZA MALA LICZBA (pozostało {0} prób)".format(próba))
    elif liczba > x:
        print("ZA DUZA LICZBA (pozostało {0} prób)".format(próba))
    else:
        if liczba == x:
            print("Brawo, wygrałeś!")
        break
else:
    print("Koniec gry, niestety przegrałeś :(")
