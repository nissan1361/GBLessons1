from time import sleep, time
import random
import sys

for itm in range(random.randint(10, 25)):
    print(itm)
    sleep(0.5)

print(sys.argv)


#def log(func):
#   def wrap(*args, **kwargs):


def some_a(x, y):
    return x + y


def some_b(x, y, z):
    return (x * y) ** z


print(some_a(1, 2))
