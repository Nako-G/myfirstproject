def procedura1():
    lista1 = [1, '2', '-5', 4 * 4, 12]
    lista2 = [1, 1, 1, 1, 1]
    lista1 = [int(i) for i in lista1]
    print("lista1=", lista1)
    print("lista2=", lista2)

    for i in lista1:
        print("Suma pierwszych elementów z listy 1 i 2")
        print("1+1=", int(lista1[0] + lista2[0]))
        break

    for i in lista1:
        print("Suma drugich elementów z listy 1 i 2")
        print("2+1=", int(lista1[1] + lista2[1]))
        break

    for i in lista1:
        print("Suma trzecich elementów z listy 1 i 2")
        print("-5+1=", int(lista1[2] + lista2[2]))
        break

    for i in lista1:
        print("Suma czwartych elementów z listy 1 i 2")
        print("4*4+1=", int(lista1[3] + lista2[3]))
        break

    for i in lista1:
        print("Suma piątych elementów z listy 1 i 2")
        print("12+1=", int(lista1[4] + lista2[4]))
        break


def procedura2():
    slownik1 = {"a": 1, "b": 2, "c": 3}
    slownik2 = {"a": 1, "c": 3, "d": 4}

def mergeDict(slownik1, slownik2):
    slownik3 = {**slownik1, **slownik2}
    print(slownik3)

    for key, value in slownik3.items():
        if key in slownik1 and key in slownik2:
            slownik3[key] = [value, slownik1[key]]

    return slownik3
    slownik3 = mergeDict(slownik1, slownik2)

    print(slownik3)




def main():
    procedura1()
    procedura2()


if __name__ == "__main__":
    main()
