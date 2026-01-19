class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus.")
        else:
            print("Bus is full! Cannot board more passengers.")

    def remove_passenger(self, person):
        if len(self.passengers) > 0:
            self.passengers.remove(person)
            print(f"{person.name} has left the bus.")
            return person
        else:
            print("Bus is empty! Cannot remove passengers.")
            return None

p1 = Person("Ana")
p2 = Person("Luis")
p3 = Person("Carlos")

bus = Bus(2)

bus.add_passenger(p1)
bus.add_passenger(p2)
bus.add_passenger(p3)

bus.remove_passenger(p1)
bus.remove_passenger(p2)
bus.remove_passenger(p3)