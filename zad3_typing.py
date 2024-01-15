def sprawdz_parzystosc(liczba):
    return liczba % 2 == 0


x = int(input("Wpisz liczbę: "))

# Przykładowe użycie funkcji

wynik = sprawdz_parzystosc(x)

# Wyświetlenie odpowiedniego komunikatu na podstawie wyniku

if wynik:

    print("Liczba parzysta")
