print("\nTen oto program dodaje do siebie dwie liczby, aż ich suma przekroczy liczbę 100")
liczba1 = int(input("\n\tPawełku, wpisz proszę pierwszą liczbę: "))
liczba2 = int(input("\tNastępnie wpisz prosze drugą liczbę: "))
print(" ")
licznik = 0
suma = 0
while suma < 200:
    if liczba1 >= 100 or liczba2 >= 100:
        print("Za wysokie liczby do tego zadania, Pawełku. Spróbuj ponownie")
        break
    if suma + liczba1 < 100:
        suma += liczba1
        licznik += 1
        print("Wynik kolejnego dodawania to: ", suma)
    if suma + liczba2 < 100:
        suma += liczba2
        licznik += 1
        print("Wynik kolejnego dodawania to: ", suma)
    if suma + liczba1 > 100 and suma + liczba2 > 100:
        break
while suma < 200:
    if suma + liczba1 > 100:
        suma += liczba1
        licznik += 1
        print("Wynik kolejnego dodawania to: ", suma)
        break
    if suma + liczba2 == 100:
        break
    if suma + liczba2 > 100:
        suma += liczba2
        licznik += 1
        print("Wynik kolejnego dodawania to: ", suma)
        break
print("\nIlość wykonanych obliczeń to: ", licznik)