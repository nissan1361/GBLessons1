class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Is Going")

    def stop(self):
        print("Is Stop")

    def turn_ridht(self):
        print("Is turning right")

    def turn_left(self):
        print("Is turning left")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, max_range):
        super(TownCar, self).__init__(speed, color, name, is_police)
        self.max_range = max_range

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Привышение скорости!!!")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, sprint):
        super(SportCar, self).__init__(speed, color, name, is_police)
        self.sprint = sprint

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, comfortable):
        super(WorkCar, self).__init__(speed, color, name, is_police)
        self.comfortable = comfortable

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("Привышение скорости!!!")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, is_alarm):
        super(PoliceCar, self).__init__(speed, color, name, is_police)
        self.is_alarm = is_alarm


car1 = Car(60, "Red", 'Honda', False)
car1.show_speed()
print(car1.name)

town_car1 = TownCar(70, "White", "BMW", False, 300)
town_car1.show_speed()
print(town_car1.color)

work_car1 = WorkCar(40, 'Black', "Gazzelle", False, "middle")
work_car1.show_speed()
work_car1.go()

police1 = PoliceCar(100, "Blue-White", "Fiat", True, True)
print(police1.color)
print(police1.is_police)
print(police1.is_alarm)
