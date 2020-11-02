count = True
user_str = []
user_input = 0
while count:
    try:
        user_input = input("Введите числа с пробелами\n>>")
    except Exception:
        print('Ошибка ввода!')

    user_str.extend(user_input.split())

    for i in user_input:
        if i == 'q':
            count = False
            user_str.pop()

    print(user_str)


summ = 0
for icount in user_str:
    int(summ)
    summ = summ + int(icount)

print(summ)
