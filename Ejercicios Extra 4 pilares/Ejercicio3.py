class Vehicle:
    def __init__(self, _brand, _year):
        self._brand = _brand
        self._year = _year

    def start_engine(self):
        return f"Engine started for {self._brand} {self._year}"

    def get_info(self):
        return f"Vehicle: {self._brand}, Year: {self._year}"

class Car(Vehicle):
    def __init__(self, _brand, _year, _doors):
        super().__init__(_brand, _year)
        self._doors = _doors

    def get_info(self):
        return f"Car: {self._brand}, Year: {self._year}, Doors: {self._doors}"

class Motorcycle(Vehicle):
    def __init__(self, _brand, _year, _type):
        super().__init__(_brand, _year)
        self._type = _type

    def get_info(self):
        return f"Motorcycle: {self._brand}, Year: {self._year}, Type: {self._type}"
    
# Example usage:
car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", 2019, "Cruiser")

print(car.get_info())
print(motorcycle.get_info())