def pelne_imie():
    """
    Funkcja pobierająca imię i nazwisko od użytkownika i zwracająca pełne imię.
    """
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    full_name = f"{name} {surname}"
    return full_name

full_name = pelne_imie()

print(f"Twoje imię i nazwisko to: {full_name}")
