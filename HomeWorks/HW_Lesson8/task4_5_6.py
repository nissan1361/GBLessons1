class Storage:
    def __init__(self, items):
        self.items = items


class HardWare:
    def __init__(self, types, weight, power):
        self.types = types
        self.weight = weight
        self.power = power

    def storage(self):
        store_list = ['3 printers', '10 pcs']



class Printer(HardWare):
    def __init__(self, types, weight, power, color):
        super(Printer, self).__init__(types, weight, power)
        self.color = color

    def print(self):
        self.color = 'black'
        self.power = 'on'

    def storage(self):
        store_list = ['3 printers']


class Pc(HardWare):
    def __init__(self, types, weight, power, cpu, gpu):
        super(Pc, self).__init__(types, weight, power)
        self.cpu = cpu
        self.gpu = gpu

    def programming(self):
        self.power = 'on'
        self.cpu = '40%'
        self.gpu = '30%'

    def storage(self):
        store_list = ['10 pcs']


printer = Printer('Cannon', 3, 'on', 'black')
printer.storage()
