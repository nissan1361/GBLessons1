from functools import reduce

mylist = []
for ls in range(100, 1001):
    if ls % 2 == 0:
        mylist.append(ls)

print(mylist)



i = 0
powers = 1
while i < len(mylist):
    powers = powers * int(mylist[i])
    i += 1

print(powers)
