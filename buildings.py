import sys
from math import *

class Budynki:
    def kosztyBudynkow(self):
        budynek = input("Wybierz żądany budynek(KM, KK, ED, EF, MM, MK, MD) ")
        poziom = int(input("Wpisz żądany poziom budynku: "))
        if budynek == "km":
            kosztMet = 60 * (15 / 10) ** (poziom - 1)
            kosztKrysz = 15 * (15 / 10) ** (poziom - 1)

            print("Metal: {}\nKryształ: {}".format(kosztMet, kosztKrysz))
