#Class notes

class Dog:

    def __init__(self, name, colour):  #dunder
        self.animal_kind = "canine"  # a dunder wont appear in drop down
        self.name = name
        self.colour = colour
        self.bark()


    def bark(self):     # Method
        print("woof")


Draco = Dog("Draco", "Green")
Draco.animal_kind = "Cat"
print(Draco.animal_kind)

# Draco = Dog()           # Instantiate a variable, print(Draco.animal_kind)
# Atticus = Dog()
#
# Atticus.animal_kind = "Rat"  # Can change class variable not bark as in function
# print(Draco.animal_kind)
# print(Atticus.animal_kind)




