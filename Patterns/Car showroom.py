import copy

class CarShowroomPrototype:
    def clone(self):
        return copy.deepcopy(self)

class CarShowroom(CarShowroomPrototype):
    def __init__(self, name, country, location, cars):
        self.name = name
        self.country = country
        self.location = location
        self.cars = cars

    def display_info(self):
        print(f"Car Showroom: {self.name}, Location: {self.location}, Country: {self.country}")
        print("Cars available:")
        for car in self.cars:
            print(f"- {car}")

if __name__ == "__main__":
    cars_in_showroom_usa = ["Toyota Camry", "Jeep Cherokee", "Honda Accord"]
    showroom_prototype = CarShowroom("BestCars", "USA", "New York", cars_in_showroom_usa)

    showroom_clone = showroom_prototype.clone()
    showroom_clone.name = "LuxuryCars"
    showroom_clone.location = "Los Angeles"
    showroom_clone.cars = ["Mercedes Benz E-Class", "BMW X5", "Lexus RX"]

    showroom_prototype.display_info()
    print("\n")
    showroom_clone.display_info()

    print("\nEnd of the program")
