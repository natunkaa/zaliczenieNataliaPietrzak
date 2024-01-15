def sprawdz_obecnosc_wartosci(lista, wartosc):
    return wartosc in lista


moja_lista = []


while True:

    wprowadzona_wartosc = input("Wpisz wartość (wpisz 'k' aby zakończyć): ")

    if wprowadzona_wartosc.lower() == 'k':
        break

    try:
        wartosc = int(wprowadzona_wartosc)
        moja_lista.append(wartosc)
    except ValueError:
        print("Wprowadź poprawną liczbę!")

print("Twoja lista:", moja_lista)

x = int(input("Wpisz liczbę do sprawdzenia: "))

wynik = sprawdz_obecnosc_wartosci(moja_lista, x)
