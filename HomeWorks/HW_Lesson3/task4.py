def my_func(x, y):
    step = x ** y
    return step

try:
    x = int(input('Введите действительное положительное число x\n>>'))
    y = int(input('Введите целое отрицательное число y\n>>'))
except Exception:
    print('Ошибка ввода!')

try:
    print(my_func(x,y))
except NameError:
    print("Ошибка")

# 2


def my_func2(x,y):
    res = x
    while y< -1:
        res = res*x

        y+= 1
    result = 1 / res
    return result

try:
    print(my_func2(x,y))
except NameError:
    print("Ошибка")
