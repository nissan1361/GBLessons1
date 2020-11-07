import json

file1 = open('file_7.txt', 'r', encoding='UTF-8')
content = file1.readlines()
my_dict = {}
for itr in content:
    data = itr.split()
    summ = int(data[1])+ int(data[2]) + int(data[3])
    my_dict[data[0]] = summ
print(my_dict)

middle_money = 0
for money in my_dict:
    middle_money = middle_money + my_dict.get(money)

middle_money = middle_money / len(my_dict)

print("Средние деньги {}".format(middle_money))
dict1 = {'Average_profit': middle_money}
my_list1 = []
my_list1.append(my_dict)
my_list1.append(dict1)
print(my_list1)

with open("file_7_json.json", "w", encoding='UTF-8') as write_f:
    json.dump(my_list1, write_f)

