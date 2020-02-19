======================================
Zadanie 3. Pseudo animacja w terminalu
======================================


Zadanie
=======

Poczatkowa tresc programu
-------------------------

.. code-block:: python

  # program3.py
  # import potrzebnych bibliotek
  import os
  import time
  import math
 
  def print_char(x, y, char):  # ta metoda mozemy wyswietlic zadany znak w terminalu w linii x poz. y
      print("\033["+str(y)+";"+str(x)+"H"+char)

  def main():
      os.system("cls") # tym poleceniem mozemy wyczyscic terminal
      # wyswietl znak '*' jak podaza po krzywej sinusoidalej w konsoli
      # do poczytania i ew uzycia metody:
      # math.sin(), time.sleep()


  if __name__ == "__main__":
     main()

