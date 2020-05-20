print("PROGRAM DO OBLICZANIA SPIRYTUSU DO NALEWEK")
print("")

print("[1] Wylicza ilość wody (alkoholu) do rozcieńczenia spirytusu aby otrzymać roztwór o zadanym stężeniu")
print("[2] Wylicza ilość spirytusu (wody) potrzebnych do sporządzenia określonej ilości roztworu o zadanym stężeniu")
print("")

def main():
    while True:
        wybor = input("Wybierz program [1] lub [2]: ")
        if wybor == "1":
            return program1()
        elif wybor == "2":
            return program2()
        else:
            print("Musisz wybrać program 1 lub 2")
            continue

def program1():
    while True:
        try:
            x = float((input("Podaj ilość spirytusu do rozcieńczenia [litry]: ")))
            if x<=0:
                print("Wartość nie może być ujemna! Spróbuj jeszcze raz")
                continue
            else:
                y = float((input("Podaj ile % ma spirytus: ")))
                if y<=0 or y>100:
                    print("Wartość musi być z przedziału 1 - 100")
                    continue
                else:
                    m = float((input("Podaj moc jaką chcesz uzyskać [%]: ")))
                    if m<=0 or m>100:
                        print("Wartość musi być z przedziału 1 - 100")
                        continue
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")
            continue
        try:
            if m > y:
                print("Nie możesz uzyskać większej mocy :(  Uruchom program jeszcze raz")
                break
            else:
                n = input("Czym chcesz rozcieńczyć spirytus? (woda, alkohol): ")
            wynik = {"woda": ((x/m)*(y-m))*1050}
            wynik1 = {"woda": ((x/m)*(y-m))*1.05}
            if n == "woda":
                print("Potrzebujesz wody do rozcieńczenia: %s [ml] (%s [litr])" % (round((wynik["woda"]), 0), (round((wynik1["woda"]),2))))
                print("Otrzymasz %s litrów roztworu" % (round(x + (round((wynik1["woda"]),2)),2)))
                break
            if n == "alkohol":
                a = float(input("Podaj ile % ma alkohol: "))
                if a<0 or a>100 or a==y:
                    print("Wartość musi być z przedziału 0 - 100 (mniejsza od % spirytusu)")
                    continue
                else:
                    wynik = {"alkohol": ((x / (m - a)) * (y - m)) * 1050}
                    wynik1 = {"alkohol": ((x / (m - a)) * (y - m)) * 1.05}
                    print("Potrzebujesz alkoholu do rozcieńczenia: %s [ml] (%s [litr])" % (round((wynik["alkohol"]), 0), (round((wynik1["alkohol"]),2))))
                    print("Otrzymasz %s litrów roztworu" % (round(x + (round((wynik1["alkohol"]), 2)), 2)))
                    break
            else:
                print("Podałeś błedną nazwę rozcieńczalnika. Spróbuj jeszcze raz")
            continue
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")


def program2():
    while True:
        try:
            x = float((input("Podaj jaką objętość roztworu chcesz otrzymać [ml]: ")))
            if x <= 0 :
                print("Wartość nie może być ujemna! Spróbuj jeszcze raz")
                continue
            else:
                y = float((input("Podaj ile % ma spirytus: ")))
                if y <= 0 or y > 100:
                    print("Wartość musi być z przedziału 1 - 100")
                    continue
                else:
                    m = float((input("Podaj moc jaką chcesz uzyskać [%]: ")))
                    if m <= 0 or m > 100:
                        print("Wartość musi być z przedziału 1 - 100")
                        continue
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")
            continue
        try:
            if m > y:
                print("Nie możesz uzyskać większej mocy :(  Uruchom program jeszcze raz")
                break
            else:
                n = input("Co chcesz dolać do spirytusu? (woda, alkohol): ")
            wynik = {"woda": ((m*x)/(m+(y-m)))}
            wynik1 = {"woda": ((m*x)/(m+(y-m)))/1000}
            wynik2 = {"woda": (y-m)*x/(m+(y-m))}
            wynik3 = {"woda": ((y-m)*x/(m+(y-m)))/1000}
            if n == "woda":
                print("Potrzebujesz spirytusu: %s [ml] (%s [litr])" % (round((wynik["woda"]), 0), (round((wynik1["woda"]),2))))
                print("Potrzebujesz dodać wody: %s [ml] (%s [litr])" % (round((wynik2["woda"]), 0), (round((wynik3["woda"]),2))))
                break
            if n == "alkohol":
                a = float(input("Podaj ile % ma alkohol: "))
                if a<0 or a>100 or a==y:
                    print("Wartość musi być z przedziału 1 - 100 (mniejsza od % spirytusu)")
                    continue
                else:
                    wynik = {"alkohol": ((m-a)*x/((m-a)+(y-m)))}
                    wynik1 = {"alkohol": ((m-a)*x/((m-a)+(y-m)))/1000}
                    wynik2 = {"alkohol": (y-m)*x/((m-a)+(y-m))}
                    wynik3 = {"alkohol": (((y-m)*x/((m-a)+(y-m))))/1000}
                    print("Potrzebujesz spirytusu: %s [ml] (%s [litr])" % (round((wynik["alkohol"]), 0), (round((wynik1["alkohol"]),2))))
                    print("Potrzebujesz dodać alkoholu: %s [ml] (%s [litr])" % (round((wynik2["alkohol"]), 0), (round((wynik3["alkohol"]),2))))
                    break
            else:
                print("Podałeś błedną nazwę rozcieńczalnika. Spróbuj jeszcze raz")
            continue
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")

if __name__ == "__main__":
   main()





