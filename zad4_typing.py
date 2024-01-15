def sprawdz_sume(arg1, arg2, arg3):

    return arg1 + arg2 >= arg3


x = int(input("Wpisz liczbę 1: "))
y = int(input("Wpisz liczbę 2: "))
z = int(input("Wpisz liczbę 3: "))

# Przykładowe użycie funkcji

arg1 = x
arg2 = y
arg3 = z
wynik = sprawdz_sume(arg1, arg2, arg3)

# Wyświetlenie wyniku

print(wynik)
