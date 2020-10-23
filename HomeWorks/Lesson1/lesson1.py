# 1

first_var = 'Hello!'
second_var = 12
var_float = 15.019
print(first_var)
print(second_var)
print(var_float)

str_var = input("Введите строку: > ")
print("Ваша строка: {}".format(str_var))

num = input("Введите число: > ")
num2 = input('Введите второе число: > ')
print('Ваши числа: {} и {} '.format(num, num2))

# 2
print('Задание 2')

time_sec = input('Введите время в секундах: > ')
time_min = 0
time_hours = 0
time_sec = int(time_sec)

i = 0

while i < time_sec:
    if time_sec >= 60:
        time_min += 1
        time_sec = time_sec - 60

    if time_min >= 60:
        time_hours += 1
        time_min = time_min - 60
    i += 1

print("Время: {} : {} : {}".format(time_hours, time_min, time_sec))

# 3
print('Задание 3')

n = input('Введите число n: > ')
nn = n + n
nnn = n + n + n

n = int(n)
nn = int(nn)
nnn = int(nnn)

res = n + nn+ nnn
print("Ответ: {}".format(res))

# 4
print('Задание 4')

integer = input('Введите целое, положительное число: > ')
clock = 0
max = 0
while clock < len(integer):
    if int(integer[clock]) > max:
        max = int(integer[clock])
    clock += 1
print("Максимальная цифра: {}".format(max))

# 5
print('Задание 5')

plus = int(input(" Введите выручку фирмы: > "))
minus = int(input(" Введите издержки: > "))
if plus > minus:
    print(" Прибыль! ")
else:
    print('Убыток!')

worker_col = int(input('Введите численность сотрудников фирмы: > '))
money_up = (plus - minus)/worker_col
print("Прибыль фирмы в расчете на одного сотрудника: {} !".format(money_up))

# 6
print('Задание 6')

a = int(input("Введите А:>"))
b = int(input('Введите B:>'))
count = 1
while a < b:
    a = a+ (a * 0.1)
    count = count + 1
print("на {} день спортсмен достиг результата — не менее {} км".format(count, b))

