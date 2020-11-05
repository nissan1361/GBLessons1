from itertools import cycle
from itertools import count

user_number = int(input("Введите начальное значение:\n>>"))
list1 = []
if user_number < 60:
    for el in count(user_number):
        if el > 60:
            break
        else:
            list1.append(el)

    print(list1)
else:
    print("Указано слишком большое число!")

# PART 2

list2 = ['a', 'b', 3]
c = 0
for el in cycle(list2):
    if c > 5:
        break
    else:
        print(el)
        c = c + 1



