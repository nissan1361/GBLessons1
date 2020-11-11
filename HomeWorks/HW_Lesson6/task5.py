class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки. ")


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print("Пишем ручкой! ")


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print("Карандашная отрисовка! ")


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print("Отрисовка маркером! ")


pen1 = Pen("Blue Pen")
pen1.draw()

pencil1 = Pencil("Gray Pencil")
pencil1.draw()

handle1 = Handle("Red Marker")
handle1.draw()
