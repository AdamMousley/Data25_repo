from Reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = False
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("smell or tastes nice")


# sidney = Snake()
# print(sidney.cold_blooded)
# sidney.seek_heat()
