class Worker:
    _income = {"Wage": 100, "Bonus": 200}

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(full_name)

    def get_total_income(self):
        total_income = self._income["Wage"] + self._income["Bonus"]
        print(total_income)


worker1 = Position("Maxim", "Petrovich", "Developer", {"Wage": 100, "Bonus": 200})
worker1.get_full_name()
worker1.get_total_income()