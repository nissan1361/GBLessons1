file1 = open('file_6.txt', 'r', encoding='UTF-8')
content = file1.readlines()
my_dict = {}
for itr in content:
    data = itr.split()
    summ = int(data[1])+ int(data[2]) + int(data[3])
    my_dict[data[0]] = summ
print(my_dict)
