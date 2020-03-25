=========================
Zadanie 10. Paczka zadan
=========================

Zadanie 1
=========
Program ma za zadanie wylosować liczbę, a użytkownik ma ją zgadnąć. Jeśli użytkownik poda mniejszą niż wylosowana - program wypisuje tekst "za mała liczba", jeśli poda większą wypisuje "za duża liczba".

Podpowiedz: https://docs.python.org/3.5/library/random.html#random.randint


Zadanie 2
=========
Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli TRÓJKĄT prostokątny o długości przyprostokątnej X,

Podpowiedz: wystarczy wyswietlanie * i spacji.

 np.: 5 ->
r"""
*
* *
*   *
*     *
* * * * *
"""

Zadanie 3
=========
Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli kwadrat z gwiazdek o długości boku X,

np.: 4 ->
r"""
*  *  *  *
*        *
*        *
*  *  *  *
"""

Zadanie 4
=========
Napisz klase "Figura" z metodami podstawowymi dla figury jak pole, obwod, przekatna.
Z tej klasy stworz kolejne (przez dziedziczenie) dla kola, prostokata, ... 
Z klasy prostokata klase kwadrat.
W klasach dziedziczacych nadpisz odpowiednie funkcje ale tylko te ktore musisz nadpisac.
Nadpisz metode __str__ tak aby klasa sie odpowiednio przedstawila przy probie wyswietlania obiektu np w sposob:
np:
kw = Kwadrat(5)
print(str(kw))
 > "Jestem kwadratem o obwodzie 20 i polu 25"

Podpowiez: https://docs.python.org/3.5/reference/datamodel.html?highlight=__str__#object.__str__
