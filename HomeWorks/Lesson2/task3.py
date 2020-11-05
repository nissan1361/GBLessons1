seasones1 = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

answer = int(input('Введите число месяца\n>>'))
if answer in seasones1[0]:
    print("Зима")
elif answer in seasones1[1]:
    print('Весна')
elif answer in seasones1[2]:
    print('Лето')
elif answer in seasones1[3]:
    print('Осень')
else:
    print("error (not a month)")

# Второй вариант:

seasones_dict = {
    1: "Зима",
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: "Зима"
}
answer2 = int(input("Введите номер месяца\n>>"))
print(seasones_dict[answer2])
