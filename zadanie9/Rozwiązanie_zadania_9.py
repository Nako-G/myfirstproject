ZADANIE_1
# Napisz program ktory sprawdzi czy podana dodatnia liczba jest potęgą "2".
print("To To jest program, który sprawdza potęgę liczby 2")
print("Wprowadź liczbę:")
n = float(input())
def PotegaLiczby(n):
    if n == 0 or n <0:
        return False
    while n != 0:
        if n % 2 != 0: #dlaczego ten warunek nie chce działać dla float???
            return False
        n = n // 2
        return True


if PotegaLiczby(int(float(n))):
    print('Ta liczba jest potęgą "2-ki"')
else:
    print('Ta liczba nie jest potęgą "2-ki"')
    
ZADANIE_2
#Napisz program ktory znajdzie najczesciej wystepujaca liczbe w podanej liscie.

list = []
liczby = int(input("Podaj ile liczb ma zawierać lista: "))
for i in range(0, liczby):
    liczby = int(input("Wpisz liczbę:"))
    list.append(liczby)

print("Twoja lista zawiera następujące liczby:", list)

def najczesciej_wystepuje(list):
    licznik = 0
    element = list

    for i in list:
        najczesciej_wystepuje = list.count(i)
        if (najczesciej_wystepuje > licznik):
            licznik = najczesciej_wystepuje
            element = i

    return element
print("Najczęściej występująca liczba w podanej liście to:",najczesciej_wystepuje(list))
