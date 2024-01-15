class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city},{self.street}," \
               f"{self.zip_code}\nOpen hours: " \
               f"{self.open_hours}\nTelephone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name,
                 hire_date, birth_date, city,
                 street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} " \
               f"{self.last_name}\nHire date: " \
               f"{self.hire_date}\nBirth date: " \
               f"{self.birth_date}\nLocation: " \
               f"{self.city}, {self.street}, " \
               f"{self.zip_code}\nPhone: {self.phone}"


class Book:
    def __init__(self, library, publication_date,
                 author_name, author_surname,
                 number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublished: " \
               f"{self.publication_date}\nPages: " \
               f"{self.number_of_pages}\n{self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"  - {book}"
                               for book in self.books])
        return f"Order:\n{self.employee}\nStudent: " \
               f"{self.student}\nOrder date: " \
               f"{self.order_date}\nBooks:{book_list}"


library1 = Library("Katowice", "Kolejowa 4", "23-334",
                   "8:00 - 20:00", "+123456789")
library2 = Library("Mysłowice", "Pokojowa 34", "25-323",
                   "10:00 - 22:00", "+987654321")

employee1 = Employee("Konrad", "Dąb", "2022-01-01",
                     "2004-05-15", "Katowice", "Kolista",
                     "20-233", "+111222333")
employee2 = Employee("Wojciech", "Gracz", "2021-02-01", "2000-07-10",
                     "Mikołów", "Mokra", "30-222", "+111111111")
employee3 = Employee("Jakub", "Michna", "2020-03-01", "2003-11-11",
                     "Mysłowice", "Polna", "12-334", "+2222222222")

book1 = Book(library1, "2023-01-01",
             "Mariusz", "Pośpiech", 299)
book2 = Book(library1, "2023-02-02",
             "Paweł", "Korona", 232)
book3 = Book(library2, "2023-03-03",
             "Gaweł", "Lorneta", 320)
book4 = Book(library2, "2023-04-04",
             "Hubert", "Mosiądz", 160)
book5 = Book(library2, "2023-05-05",
             "Ula", "Piasecka", 170)

order1 = Order(employee1, "Student1",
               [book1, book3, book5], "2023-01-15")
order2 = Order(employee2, "Student2",
               [book2, book4], "2023-02-20")

print(order1)
print("\n---------------------------\n")
print(order2)
