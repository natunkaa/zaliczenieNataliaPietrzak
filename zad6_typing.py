def polacz_i_przetworz(list1, list2):
    polaczona_lista = list1 + list2
    unikalna_lista = list(set(polaczona_lista))
    przetworzona_lista = [x**3 for x in unikalna_lista]
    return przetworzona_lista

# Przykład użycia:
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
wynik = polacz_i_przetworz(lista1, lista2)
print(wynik)
