class Car:
    def __init__(self, name, vin):
        self.name = name
        self.vin = vin

class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def set_car(self, *cars):
        self.__box.extend(cars)

    def __getitem__(self, item):
        return self.__box[item]

