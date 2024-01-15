print("a.")

# a.
def lista_imion(imiona):
    for imie in imiona:
        print(imie)

imiona = ["Łukasz", "Jakub", "Adam", "Agnieszka", "Robert"]
lista_imion(imiona)

print("x.")

# x.1
def pomnoz_elementy(lista):
    wynik = []
    for element in lista:
        wynik.append(element * 2)
    return wynik

liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_elementy(liczby)
print(wynik)

print("x.2")

# x.2
def pomnoz_elementy_lista_skladana(lista):
    return [element * 2 for element in lista]

wynik_lista_skladana = pomnoz_elementy_lista_skladana(liczby)
print(wynik_lista_skladana)

print("y.")

# y.
def wyswietl_parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

liczby_parzyste = list(range(1, 11))
wyswietl_parzyste(liczby_parzyste)

print("d.")

# d.
def wyswietl_co_drugi_element(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

liczby = list(range(1, 11))
wyswietl_co_drugi_element(liczby)
