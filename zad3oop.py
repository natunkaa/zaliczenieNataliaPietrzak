class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"property: {self.area} sq. meters, {self.rooms} rooms\n" \
               f"price: ${self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"house: {self.area} sq. meters, {self.rooms} rooms\n" \
               f"price: ${self.price}\nAddress: {self.address}\n" \
               f"plot: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"flat: {self.area} sq. meters, {self.rooms} rooms\n" \
               f"price: ${self.price}\nAddress: {self.address}\n" \
               f"floor: {self.floor}"


house_obj = House(area=150, rooms=5, price=200000, address="123 Main Street",
                  plot=500)

flat_obj = Flat(area=80, rooms=3, price=120000, address="456 Oak Avenue", floor=2)

print("house:")
print(house_obj)

print("\nflat:")
print(flat_obj)
