# myfirstproject
sample project
print("Lista podzespołów drona_1:")
elektronika = ["Motor","Motor","Motor","Motor","ESC","ESC","ESC","PDB","FC","Receiver RX", "Transmitter VTX", "Camera receiver VTX","Camera"]
elektronika.insert(7,"ESC")
pozostałe = ["Frame","Propellers","Antenna","Antenna","Radiator"]
pozostałe.append("Buzzer")
pozostałe.append("LED lights")

Battery1 = [1300,1400,1500,1350]
Battery2 = [1500,1600,1500,1500]
pozostałe.remove("Radiator")
elektronika.extend(pozostałe)
elektronika.extend(Battery1+Battery2)
for i in Battery1:
    if i == 1300:
        print("Battery 1300mAh")
    elif i == 1500:
        print("Battery 1500mAh")
    else:
        print("Baterry_unknown")

for i in Battery2:
    if i != 1500:
        print("This battery doesn't exist")


print(*elektronika, sep="\n")

print("Zestawienie ilościowe")
szer = 38
print("-"*szer)
print("|      Rodzaj            |   Ilość   |")
print("*"*szer)
print("| %7s                | %9s |" % ("Silniki", elektronika.count("Motor")))
print("| %10s             | %9s |" % ("Regulatory", elektronika.count("ESC")))
print("| %6s                 | %9s |" % ("Anteny", elektronika.count("Antenna")))
print("-"*szer)
