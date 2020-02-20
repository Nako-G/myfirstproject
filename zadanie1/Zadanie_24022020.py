lista1 = [1, '2', '-5', 4*4, 12]
lista2 = [1, 1, 1, 1, 1]
lista1 = [int(i) for i in lista1]

print("\n" "Wymagany warunek: wartość z listy1> wartośći z listy2")

for i in range(len(lista2)):
    a = lista1[i]
    b = lista2[i]
    if b>a:
        print("\n" "Wartość %s z listy1 spełnia wymagany warunek" %b)
    else:
        print("\n" "Ta pozycja z listy1 nie spełnia wymaganego warunku")
