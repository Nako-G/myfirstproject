class Argumenty:
    def __init__(self):
        pass

    def metoda1(self,x,y):
        if int == type(x) and int == type(y):
            print(x**y)
        elif str == type(x) and int == type(y):
                print(x*y)
        elif list == type(x):
            lista2 = []
            for i in x:
                if type(i) == int:
                    lista2.append(i)
            print(max(lista2))
        else:
            pass
        if int != type(y):
            pass

a = Argumenty()
a.metoda1([3,5,"a",3,7],2)
