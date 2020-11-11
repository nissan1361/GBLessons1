class Car:
    _cars = []
    # brand = ''
    # color = ''
    vin = ''

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self._cars.append(self)

    def Start_Engine(self):
        print("Wroom, Wroom")

car1 = Car('ford', 'blue')
# car1.brand = 'Ford'
# car1.color = 'blue'


car2 = Car('mazda', 'red')
# car2.brand = 'Mazda'
# car2.color = 'red'

# Car.vin = '12345'
# Car.color = 'white'

print(car1.brand)
print(car1.color)


class ElectroCar(Car):
    def __init__(self, brand, color, engine):
        super().__init__(brand, color)
        self.engine = engine

    def bip(self):
        print('Bip Bip')

    def Start_Engine(self):
        print("SSSSS IIIII")
        super(ElectroCar, self).Start_Engine()


elcar = ElectroCar("Tesla", "red", "2000kwt")
elcar.Start_Engine()


class Robot:
    def __init__(self, name, rtype):
        self.name = name
        self.rtype = rtype


class Transformer(Car, Robot):
    def __init__(self, name):
        super().__init__("ufo", 'multi')
        Robot.__init__(self, 'Optimus', 'Truck')
        self.__is_transform = True

    def Start_Engine(self):
        if self.__is_transform:
            print("Optimus")
        else:
            super().Start_Engine()

    def transformation(self):
        print("Transform!")
        self.__is_transform = not self.__is_transform


optimus = Transformer("Optimus Prime")
optimus.Start_Engine()

optimus.transformation()
optimus.Start_Engine()