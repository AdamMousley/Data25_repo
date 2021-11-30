class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude      # self means its refered to this class
        self.longitude = longitude    # self.___ exists everywhere in the class

    def __repr__(self):
        return f"Location=(longitude={self.longitude}, latitude={self.latitude})"

    # def __str__(self):  # designed to give readable human output
    #     return f"{self.latitude}, {self.longitude}"

bham_academy = Location(52.488647, -1.887249)
print(bham_academy)