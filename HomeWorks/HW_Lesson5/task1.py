file = open('text1.txt', 'w', encoding='UTF-8')

check = True
while check:
    f_string = input("Введите строку в файл >> ")
    file.writelines(f_string)
    file.write("\n")
    if f_string == '':
        check = False

file.close()

file2 = open('text1.txt', 'r', encoding='UTF-8')
print(file2.read())
file2.close()
