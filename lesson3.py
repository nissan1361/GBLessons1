"""
sum()
map()
reduce()
min()
max()
enumerate()
zip()
"""


def my_sum(a, b):
    """my sum func for two vars
    :param a int or float
    :param b int or float
    :return sum a and b
    """
    result = a + b
    return result


def some(a: int) -> int:
    return a**3


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def my_map(func, iter_obj):
    result = []
    for itm in iter_obj:
        result.append(func(itm))
    return result


def some_tree(name, surname):
    return f'fullname: {name},{surname}'


def some_for(*args):
    print(type(args))
    return sum(args)
