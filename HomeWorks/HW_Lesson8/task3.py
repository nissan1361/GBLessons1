class OnlyNums:
    def __init__(self, itm):
        self.itm = itm

    def function_ex(self):
        error1 = True
        try:
            int(self.itm)
            return False
        except ValueError:
            error1 = True
            return error1


list1 = []
while True:
    inp_itm = input("Введите число: \n:>>")
    only_num = OnlyNums(inp_itm)
    tracker = only_num.function_ex()
    if not tracker:
        list1.append(inp_itm)
    print("чтобы выйти введите stop")

    if inp_itm == 'stop':
        break

print(list1)