from Country import Country

class City(Country):

    def __init__(self,city_name, country_name, climate, continent, language):
        super().__init__(country_name, continent, climate, language)
        self.city_name = city_name

    def beaches(self):
        print("Yes we have lovely beaches")

    def food(self):
        print("You want souvlaki? Taziki?")

city_info = City("Athens", "Greece", "Hot", "Europe", "Greek")

print(city_info.city_name)
city_info.beaches()
city_info.food()