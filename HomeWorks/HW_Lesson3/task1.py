def myFunc(a,b):
    result = 0
    if b != 0:
        result = a / b
        return  result
    else:
        return "Деление на ноль!"
try:
    a = int(input('Введите делимое\n>>'))
except Exception:
    print('Ошибка ввода!')

try:
    b = int(input('Введите делитель\n>>'))
except Exception:
    print('Ошибка ввода!')

try:
    print(myFunc(a,b))
except NameError:
    print("Ошибка")
