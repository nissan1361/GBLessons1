lorem = 'abvgd, 123 abcde fff ggg'

file = open('lorem.txt', 'w', encoding='UTF-8')
file.write(lorem)
file.close()

file_read = open('lorem.txt', 'r', encoding='UTF-8')
print(file_read.read())
file.close()
