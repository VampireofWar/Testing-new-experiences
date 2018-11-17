import sys
from math import sqrt

class Surowce:
    def wytwarzanieSurowcow(self):
        poziomMet = int(input("Podaj poziom rozbudowania kopalni metalu: "))
        poziomKrysz = int(input("Podaj poziom rozbudowania kopalni kryształu: "))
        poziomDeut = int(input("Podaj poziom rozbudowania ekstraktora deuteru: "))
        tempP = int(input("Podaj temperaturę planety: "))

        wydobMet = 30 * poziomMet * (11 / 10) ** poziomMet
        wydobKrysz = 20 * poziomKrysz * (11 / 10) ** poziomKrysz
        wytwDeut = 10 * poziomDeut * (11 / 10) ** poziomDeut * ((144 / 100) - (4 / 1000) * tempP)

        print("\nWydobycie metalu: {}/h\nWydobycie kryształu: {}/h\nWytwarzanie deuteru: {}/h".format(wydobMet, wydobKrysz, wytwDeut))
    def wytwarzanieEnergii(self):
        poziomElekSlon = int(input("Podaj poziom rozbudowania elektrowni słonecznej: "))
        poziomElekFuz = int(input("Podaj poziom rozbudowania elektrowni fuzyjnej: "))
        iloscSat = int(input("Podaj ilość aktywnych satelitów słonecznych: "))
        tempP = int(input("Podaj temperaturę planety: "))
        poziomTechEner = int(input("Podaj poziom technologii energetycznej: "))

        wytwEnerSlon = 20 * poziomElekSlon * (11 / 10) ** poziomElekSlon
        wytwEnerFuz = 30 * poziomElekFuz * ((105 / 100) + poziomTechEner * (1 / 100)) ** poziomElekFuz
        wytwEnerSat = (tempP + 140) / 6 * iloscSat
        wytwEnerSum = wytwEnerSlon + wytwEnerFuz + wytwEnerSat

        print("Aktualne wytwarzanie energii wynosi {} jednostek, na które składa się:\n{} z elektrownii słonecznej\n{} z elektrownii fuzyjnej\n{} z satelitów słonecznych".format(wytwEnerSum, wytwEnerSlon, wytwEnerFuz, wytwEnerSat))
