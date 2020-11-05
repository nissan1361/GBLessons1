import random

my_list = []
for i in range(15):
    my_list.append(random.randint(0,20))

print(my_list)

final_list = []

i = 1
while i < len(my_list):
    if my_list[i] > my_list[i - 1]:
        final_list.append(my_list[i])
    i += 1

print(final_list)

