def procedura1():
  lista1 = [1, '2', '-5', 4 * 4, 12]
  lista2 = [1, 1, 1, 1, 1]
  lista1 = [int(i) for i in lista1]
  print("lista1 =", lista1)
  print("lista2 =", lista2)
  print("\n" "Suma elementów listy1 oraz listy2")


  for i in range(len(lista1)):
    a = lista1[i]
    b = lista2[i]
    print("Dla %s+%s=%s" %(a,b,a+b))

  print("\n" "-------------------------------------")
def procedura2():  
  slownik1 = {"a": 1, "b": 2, "c": 3}
  slownik2 = {"a": 1, "c": 3, "d": 4}
  print("\n" "slownik1 = ", slownik1)
  print("slownik2 = ", slownik2)

  print("\n" "a) Unikalna lista kluczy slownika1 oraz slownika2:")
  print("slownik1 + slownik2 =", set(list(slownik1.keys())+list(slownik2.keys())))
  klucze = (list(set(list(slownik1.keys())+list(slownik2.keys()))))

  print("\n" "b) slownik zawierającay liste kluczy:")
  for i in klucze:
    a = (slownik1.get(i,0))
    b = (slownik2.get(i,0))
    wartosci = (a + b)
  
    print("Wartość dla klucza %s=>%s" %(i,wartosci) )

def main():
   """ To jest glowna procedura/funkcja programu uruchamiana ponizej. """
   procedura1()
   procedura2()

if __name__ == "__main__":
   main()
