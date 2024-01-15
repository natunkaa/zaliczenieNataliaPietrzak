def sprawdz_parzystosc(liczba):
    return liczba % 2 == 0

# Wczytanie liczby od użytkownika
x = int(input("Wpisz liczbę: "))

# Przykładowe użycie funkcji
wynik = sprawdz_parzystosc(x)

# Wyświetlenie odpowiedniego komunikatu na podstawie wyniku
if wynik:
    print("Liczba parzysta"
