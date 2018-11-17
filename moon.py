import sys
from math import sqrt

class MoonEvents:
    def szansaZniszczen(self):
        srednicaK = int(input("\nPodaj średnicę Księżyca: "))
        liczbaGS = int(input("Podaj liczbę Gwiazd Śmierci: "))

        szansaZniszczeniaK = (100 - sqrt(srednicaK)) * sqrt(liczbaGS)
        szansaZniszczeniaGS = (sqrt(srednicaK)) / 2

        szansaZniszczeniaK = round(szansaZniszczeniaK, 0)
        szansaZniszczeniaGS = round(szansaZniszczeniaGS, 0)

        print("\nSzansa zniszczenia Księżyca wynosi {} % \nSzansa na zniszczenie Gwiazdy Śmierci wynosi {} %\n".format(szansaZniszczeniaK, szansaZniszczeniaGS))
