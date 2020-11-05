import random

my_list = []
for ls in range(1, 45):
    my_list.append(random.randint(0,20))

print(my_list)

list2 = set(my_list)
print(list2)
