from random import random, randint

m = int(input("Vloz horni hranici hadaneho cisla:"))
nahodne_cislo = randint (0,m)

kolikrat_hadal = 0

hadej = True

while hadej == True:
    hadane_cislo = int(input("Zadej cislo ktere si myslis:"))
    kolikrat_hadal += 1
    if hadane_cislo == nahodne_cislo:
        print("Uhadnul jsi na:")
        print(kolikrat_hadal)
        break
    elif hadane_cislo > nahodne_cislo:
        print("Hadane cislo je vetsi nez nahodne cislo")
    elif hadane_cislo < nahodne_cislo:
        print("Hadane cislo je mensi nez nahodne cislo")

    hadej == False

