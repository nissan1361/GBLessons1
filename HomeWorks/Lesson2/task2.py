list_1 = []
count = 0
while count < 10:
    list_1.append(input("Введите элемент списка\n>>"))
    count += 1
print(list_1)

# Обмен
changed = 0
count2 = 1
while count2 < 10:
    changed = list_1[count2-1]
    list_1[count2-1] = list_1[count2]
    list_1[count2] = changed
    count2 += 2
print(list_1)
