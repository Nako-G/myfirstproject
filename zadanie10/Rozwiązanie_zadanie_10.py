ZADANIE 1

import random
x = random.randrange(1, 10)

print("Znajdź liczbę z przedziału od 1 do 10 w trzech ruchach i wygraj nagrodę!")
próba = 2
for próba in range(próba, -1, -1):
    liczba = int(input("Wpisz liczbę: "))

    if liczba < x:
        print("ZA MALA LICZBA (pozostało {0} prób)".format(próba))
    elif liczba > x:
        print("ZA DUZA LICZBA (pozostało {0} prób)".format(próba))
    else:
        if liczba == x:
            print("Brawo, wygrałeś!")
        break
else:
    print("Koniec gry, niestety przegrałeś :( Szukana liczba to: ", x)
    
    
ZADANIE 2
x = int(input("Podaj długość przyprostokątnej: "))
for x in range(0, x):
    print((x+1) * "*")
    
ZADANIE 3
x = int(input("Podaj długość boku kwadratu: "))

for i in range(x):
    for i in range(x):
        print("*", end="  ")
    print()
    
ZADANIE 4
