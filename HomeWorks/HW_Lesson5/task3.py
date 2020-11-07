file1 = open('file_task3.txt', 'r', encoding='UTF-8')
content = file1.readlines()
# print(content)

for itr in content:
    data = itr.split()

#    print(data)

    if int(data[1]) < 20000:
        print(data[0], " Получает {} , что меньше 20 тысяч".format(data[1]))

middle_money = 0
i = 1
for sr in content:
    data2 = sr.split()

    middle_money = middle_money + int(data2[1])
    i += 1

middle_money = middle_money / i
print("Средний доход сотрудников: {} рублей.".format(round(middle_money)))

file1.close()