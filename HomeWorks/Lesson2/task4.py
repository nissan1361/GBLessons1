user_string = input('Ведите строку с пробелами\n>>')
i = 1
for stri in user_string.split():
    print(i, ' ', stri)
    i += 1
