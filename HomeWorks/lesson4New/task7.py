

def fact_gen(n):
    if n == 1:
        return 1
    else:
        return n * fact_gen(n -1)


num = int(input("Введите число\n>>"))
print(fact_gen(num))