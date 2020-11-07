file = open('file_5.txt', 'w', encoding='UTF-8')

file.write("1 2 3 4 5")
file.close()
file1 = open('file_5.txt', 'r', encoding='UTF-8')

content = file1.read()
spl = content.split()
print(spl)
summ = 0
for sp in spl:
    summ = summ + int(sp)

print('Сумма: {} '.format(summ))

