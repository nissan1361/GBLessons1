def int_func(string: str):
    u_str = []
    u_str.extend(string.title().split())
    return u_str


str1 = ''

try:
    str1 = input('Введите строку\n>>')
except Exception:
    print('Ошибка ввода!')

print(int_func(str1))

