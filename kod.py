import random

szukana = random.randint(1,100)
liczba = int(input("Wylosowano liczbę z przedziału od 1 do 100. Zgadnij jaka to liczba: "))

proby = 1

while liczba!= szukana:
    if liczba>szukana:
        print("Wylosowana liczba jest mniejsza, spróbuj ponownie.")
    elif liczba<szukana:
        print("Wylosowana liczba jest większa, próbuj dalej.")

    liczba = int(input("Spróbuj ponownie: "))
    proby =+1

print("Gratulacje! Zgadłeś wylosowaną liczbę: ", szukana,".","Potrzebowałeś do tego: ", proby, "prób")
