================================================
Zadanie 2. listy, dicty, itp. Utwalenie zadania1
================================================


Zadanie
=======

Poczatkowa tresc programu
-------------------------

.. code-block:: python

  # program2.py
  def procedura1():
     lista1 = [1, '2', '-5', 4*4, 12]
     lista2 = [1, 1, 1, 1, 1]
     # wyswietl elementy z listy 2 ale tylko takie ktorych wartosc jest wieksza 
     # niz odpowiadajacy mu indexem element w liscie 1
  
  def procedura2():
     slownik1 = {"a": 1, "b": 2, "c": 3}
     slownik2 = {"a": 1, "c": 3, "d": 4}
     lista1 = ['a', 'b', 'x', 'd']
     # wyswietl klkucz => wartosc z slownik1 i slownik2 dla odpowiadajacych im kluczy w lista1
 
   def procedura3():
     slownik1 = {"a": 1, "b": 2, "c": 3}
     slownik2 = {"a": 1, "c": 3, "d": 4}
     lista1 = ['a', 'b', 'x', 'd']
     # stworz slownik z kluczami z lista1. Wartosc dla klucza to najwieksza wartosc ze slownik1 lub slownik2 lub 0.
     # wyswietl ten slownik
 
  def main():
     """ To jest glowna procedura/funkcja programu uruchamiana ponizej. """
     procedura1()
     procedura2()
     procedura3()
  
  if __name__ == "__main__":
     main()

