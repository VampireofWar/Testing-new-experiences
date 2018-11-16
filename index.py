import sys
import random

ans = True

while ans:
    question = raw_input("Magiczna kula prawdę ci powie (wciśnij Enter aby wyjść)")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print "Zależy"

    elif answers == 2:
        print "Raczej na pewno tak"

    elif answers == 3:
        print "Prawdopodobnie"

    elif answers == 4:
        print "Zapytaj później"

    elif answers == 5:
        print "Nie wiem"

    elif answers == 6:
        print "Moje źródła mówią: nie"

    elif answers == 7:
        print "No chyba nie..."

    elif answers == 8:
        print "Mocne i stanowcze: nope"
