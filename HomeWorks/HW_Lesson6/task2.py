class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_road(self, mass_for_1_km, thickness):
        result = self.length * self.width * mass_for_1_km * thickness
        print(result)


hi_way = Road(5000, 20)
hi_way.mass_road(25, 5)