print("lesson2")

some_list = [1, 2, 3, 4, [1, 2, 5, 1]]

some_list.append("NEW")
print(some_list)

some_string = "asdfghj"
print('d' in some_string)

some_list.pop()
print(some_list)

some_set = {1, 1, 2, 3, 4, 3, 2, 1, 2, 2, 3}
print(some_set)
some_set2 = {5, 6, 7, 8, 1}
print(some_set & some_set2)

some_dict = {'key1': 'Hello', 'key2': 222}
print(some_dict['key1'])

template = {
    'name': 'Ваше имя \n>>',
    'surname': 'Ваша фамилия \n>>',
    'city': 'Ваш город \n>>'
}
user = {}
for key, value in template.items():
    user[key] = input(value)
