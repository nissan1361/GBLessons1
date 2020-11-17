class NullDel:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def function(self):
        try:
            result = self.num1/self.num2
            return result
        except Exception:
            return 'На "0" Делить Нельзя!'


num_1 = float(input("Введите делимое: \n>>"))
num_2 = float(input("Введите делитель: \n>>"))
my_del = NullDel(num_1, num_2)

print(my_del.function())
