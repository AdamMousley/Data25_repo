from pokemon_type import water_type
from pokemon_type import fire_type
from pokemon_type import grass_type

class pokemon_name(water_type):
    def __init__(self, water):
        super().__init__(self, water)

    def water_gun(self):
        print("Attack move- Water gun did 10 damage")

    def rest(self):
        print("Squirtle rested and gained 10 health")

    def scald(self):
        print("Attack move- Scald did 25 damage")

    def surf(self):
        print("Attack move- Surf did 15 damage")

class pokemon_name2(fire_type):
    def __init__(self,fire):
        super().__init__(self,fire)

    def flamethrower(self):
        print("Attack move- Flamethrower did 10 damage")

    def rest(self):
        print("Charmander rested and gained 10 health")

    def fire_punch(self):
        print("Attack move- Fire punch did 25 damage")

    def ember(self):
        print("Attack move- Ember did 15 damage")

class pokemon_name3(grass_type):
    def __init__(self, grass):
        super().__init__(self, grass)

    def razor_leaf(self):
        print("Razor leaf did 10 damage")

    def rest(self):
        print("Charmander rested and gained 10 health")

    def solar_beam(self):
        print("Solar_beam did 25 damage")

    def poison_spore(self):
        print("Poison spore did 15 damage, luckily you're not poisoned")

# squirtle = pokemon_name("Water")
# squirtle.water_gun()
#
# charmander = pokemon_name2("Fire")
# charmander.flamethrower()
#
# bulbasaur = pokemon_name3("Grass")
# bulbasaur.razor_leaf()