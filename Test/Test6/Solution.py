class Vehicle:
     def __init__(self):
        if type(self) == Vehicle:
            raise TypeError("Vehicle object cannot be created")
    def calculate_toll(self):
        print("Calculate toll")
class TwoWheeler(Vehicle):
    def __init__(self, persons):
        super().__init__()
        self.persons = persons
    def calculate_toll(self):
        toll = 20
        if self.persons > 2:
            extra_persons = self.persons - 2
            toll = toll + extra_persons * 10
        return toll


class ThreeWheeler(Vehicle):

    def __init__(self, persons):
        super().__init__()
        self.persons = persons

    def calculate_toll(self):
        toll = 30

        if self.persons > 3:
            extra_persons = self.persons - 3
            toll = toll + extra_persons * 20

        return toll


class FourWheeler(Vehicle):

    def __init__(self, persons):
        super().__init__()
        self.persons = persons

    def calculate_toll(self):
        toll = 40

        if self.persons > 4:
            extra_persons = self.persons - 4
            toll = toll + extra_persons * 40

        return toll


class HeavyVehicle(Vehicle):

    def __init__(self, persons):
        super().__init__()
        self.persons = persons

    def calculate_toll(self):
        toll = 60

        if self.persons > 6:
            extra_persons = self.persons - 6
            toll = toll + extra_persons * 100

        return toll


# Main program

while True:

    print("\n========== TOLL MENU ==========")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        persons = int(input("Enter number of persons: "))
        vehicle = TwoWheeler(persons)

    elif choice == 2:

        persons = int(input("Enter number of persons: "))
        vehicle = ThreeWheeler(persons)

    elif choice == 3:

        persons = int(input("Enter number of persons: "))
        vehicle = FourWheeler(persons)

    elif choice == 4:

        persons = int(input("Enter number of persons: "))
        vehicle = HeavyVehicle(persons)

    elif choice == 5:

        print("Thank you!")
        break

    else:

        print("Invalid choice")
        continue
    print("Total Toll =", vehicle.calculate_toll())
