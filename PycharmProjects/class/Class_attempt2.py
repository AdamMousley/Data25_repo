class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, color):
        self.make = make        #  instance variable
        self.model = model      #  initilization
        self.year = year
        self.color = color


car_1 = Car("Chevy", "Corvette", 2021, "blue")  #  Instatuate
car_2 = Car("Ford", "Mustang", 2022, "red")

Car.wheels = 2
print(Car.wheels)

print(car_1.wheels)
print(car_2.wheels)

print(car_1.make)