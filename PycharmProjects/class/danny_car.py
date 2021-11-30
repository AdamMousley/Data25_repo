class Car:

    def __init__(self, colour, max_speed, min_speed, num_of_wheels, wings):
        self.current_speed = 0
        self.colour = colour
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.num_of_wheels = num_of_wheels
        self.wings = wings

    def accelerate(self, speed_to_accelerate):
        if self.current_speed + speed_to_accelerate > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_to_accelerate
        return self.current_speed

    def dec(self, speed_to_dec):
        if self.current_speed - speed_to_dec < self.min_speed:
            self.current_speed = self.min_speed
        else:
            self.current_speed -= speed_to_dec
        return self.current_speed

    def nitros(self, boost, boost_time, current_speed):
        if boost == True:
            boost_factor = 0.1
            acceleration_factor = boost_time * boost_factor
            self.current_speed = (self.current_speed * acceleration_factor) + self.current_speed
            return self.current_speed

    def softop(self, weather):
        self.weather = weather
        if weather == "Sunny":
            return "Softtop is up"
        else:
            return "Softtop is down"
    def fly(self, wings, current_speed):
        self.wings = wings
        self.current_speed = current_speed
        if current_speed > 150 and wings is True:
            return "We're Flying Boizzz"
        elif current_speed <= 150 and wings == True:
            current_speed = self.nitros(True, 20, current_speed)
            return 'Nitro boost to fly!'
        else:
            wings = False
            return wings


class Circuit:

    def __init__(self, distance):
        self.distance = distance


# Zohra's Car
Zohrehs_Car = Car("Purple", 200, 0, 4, True)


# Danny's Car
Dannys_Car = Car("Green", 1000, 0, 4, True)
print(Dannys_Car.fly(True,160))

# Zohra's Car
Zohrehs_Car = Car("Purple", 200, 0, 4, True)
print("----- Zohreh's Car -----")
print(f'Colour: {Zohrehs_Car.colour}')
print(f'Max Speed: {Zohrehs_Car.max_speed}')
print(f'Min Speed: {Zohrehs_Car.min_speed}')
print(f'Number of Wheels: {Zohrehs_Car.num_of_wheels}')
print()
print()
# Danny's Car
Dannys_Car = Car("Green", 1000, 0, 4, True)
print("----- Danny's Car -----")
print(f'Colour: {Dannys_Car.colour}')
print(f'Max Speed: {Dannys_Car.max_speed}')
print(f'Min Speed: {Dannys_Car.min_speed}')
print(f'Number of Wheels: {Dannys_Car.num_of_wheels}')