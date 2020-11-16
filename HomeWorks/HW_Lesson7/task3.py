class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return Cell(self.count - other.count)
        else:
            raise ValueError('Не верное количество клеток')

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self):
        cells = ''
        for cell in self.count:
            cells = cells + '*'
        cells += "\n"

    def __str__(self):
        return f"Клеток ({self.count})"


cnt = input("Введите Количество клеток (int): \n>>")
cnt2 = input("Введите Количество клеток 2 (int): \n>>")
sells = Cell(int(cnt))
sells2 = Cell(int(cnt2))

print(sells + sells2)
if sells.count < sells2.count:
    raise ValueError('Не верное количество клеток')
else:
    print(sells - sells2)
print(sells * sells2)
print(sells / sells2)