my_list = [7, 5, 3, 3, 2]
user_num = int(input("Введите новый элемент list\n>>"))
my_list.append(user_num)

sortes_list = sorted(my_list, reverse=True)

print(sortes_list)
