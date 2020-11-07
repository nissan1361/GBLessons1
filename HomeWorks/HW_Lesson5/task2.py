file1 = open('file_task2.txt', 'r', encoding='UTF-8')
content = file1.readlines()
str_count = len(content)
print('Количество строк: {} '.format(str_count))
i = 1
for itr in content:
    words = itr.split()
    word_count = len(words)
    print("Количество слов в {} строке: {} ".format(i, word_count))
    i += 1

file1.close()
