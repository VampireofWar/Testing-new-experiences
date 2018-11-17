import sys
import moon
import resources
import buildings

ans = True
while ans:
    print("1. Księżyc\n2. Surowce\n3. Budynki\n0. Wyjdź")
    ans = input("Wybierz opcję: ")
    if ans == "1":
        ans1 = moon.MoonEvents()
        ans1.szansaZniszczen()
    if ans == "2":
        sur = True
        while sur:
            ans2 = resources.Surowce()
            print("\n1. Kalkulacja wydobycia\n2. Kalkulacja wytwarzania energii\n0. Powrót")
            sur = input("Wybierz opcję: ")
            if ans == "1":
                ans2.wytwarzanieSurowcow()
            if ans == "2":
                ans2.wytwarzanieEnergii()
            if ans == "0":
                exit()
    if ans == "3":
        ans3 = buildings.Budynki()
        ans3.kosztyBudynkow()
    if ans == "0":
        exit()
