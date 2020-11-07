file1 = open('file_4.txt', 'r', encoding='UTF-8')
file2 = open('file_4_2.txt', 'w', encoding='UTF-8')
content = file1.readlines()

for itr in content:
    data = itr.split()
    if data[0] == "One":
        file2.write("Один - " + data[2] + '\n')
    elif data[0] == "Two":
        file2.write("Два - " + data[2] + '\n')
    elif data[0] == "Three":
        file2.write("Три - " + data[2] + '\n')
    elif data[0] == "Four":
        file2.write("Четыре - " + data[2] + '\n')

file2.close()
file1.close()
