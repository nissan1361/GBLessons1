def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    sum = my_list[1] + my_list[2]
    return sum


try:
    a = int(input('Введите A\n>>'))
    b = int(input('Введите B\n>>'))
    c = int(input('Введите C\n>>'))
except Exception:
    print('Ошибка ввода!')


try:
    print(my_func(a,b,c))
except NameError:
    print("Ошибка")

