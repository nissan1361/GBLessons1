struct = [
    (1, {'имя': 'pc', 'цена': 40000}),
    (2, {'имя': 'iphone', 'цена': 70000}),
    (3, {'имя': 'xerox', 'цена': 10000})
]
for k,v in struct:
    print(v.get('имя'),v.get('цена'))