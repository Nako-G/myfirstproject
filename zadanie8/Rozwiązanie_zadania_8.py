class Argumenty:
    def __init__(self):
        pass

    def metoda1(self,x,y):
        if int == type(x) and int == type(y):
            print(x**y)
        elif str == type(x) and int == type(y):
                print(x*y)
        elif list == type(x):
            print(max(list(x)))
        else:
            pass
        if int != type(y):
            pass

a = Argumenty()
a.metoda1(3,2)
