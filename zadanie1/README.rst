==========================
Zadanie 1. Konwersja typow
==========================


Zadanie
=======

Poczatkowa tresc programu
-------------------------

.. code-block:: python

  # program1.py
  def czesc1():
     lista1 = [1, '2', '-5', 4*4, 12]
     lista2 = [1, 1, 1, 1, 1]
     # wyswietl sume elementow tych list jeden po drugim ( pierwszy z pierwszym, drugi z drugim, ... )
     # uzyj petli for
     # calosc wyswietl w formie dzialan np 1 + 1 = 2 linijka pod linijka
  
  def czesc2():
     slownik1 = {"a": 1, "b": 2, "c": 3}
     slownik2 = {"a": 1, "c": 3, "d": 4}
     # slownik (dict) to zbior elementow klucz => wartosc.
     # a. wyswietl unikalna liste kluczy z obydwu tych slownikow laczenie ( podpowiedz: set, keys, '+' )
     # b. stworz i wyswietl slownik ktory zawiera wszystkie klucze z obydwu powyzszych slownikow
     # wartosci powinny byc suma odpowiadajacych im wartosci czyli np dla "a" wartoscia bedzie 2
     # podpowiedz: dict.get
     # wynik wyswietl w formie "klucz" => "wartosc" linijka pod linijka
  
  def main():
     """ To jest glowna funkcja programu uruchamiana ponizej. """
     czesc1()
     czesc2()
  
  if __name__ == "__main__":
     main()

Opis
----
W tym programie do opanowania jest umiejesnosc:

- tworzenia i wywolywania funkcji
- formatowania w print
- uzycia petli for oraz zmiennej pomocniczej do wyciagania elementow listy
- uzycia typu 'set' oraz konwersji z i do listy
- uzycia metody metody 'get' obiektu dict 

