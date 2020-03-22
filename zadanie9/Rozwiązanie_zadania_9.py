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
