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
        

slownik1 = {"a": 1, "b": 2, "c": 3}
slownik2 = {"a": 1, "c": 3, "d": 4}
lista1 = ['a', 'b', 'x', 'd']
print("slownik1=",slownik1)
print("slownik1=",slownik2)
print("lista1", lista1)
print("\n")
for i in lista1:
   a = (slownik1.get(i,0))
   b = (slownik2.get(i,0))
   print("Wartość dla klucza %s: %s+%s=%s" %(i,a,b,a+b))
