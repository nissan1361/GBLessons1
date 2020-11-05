def my_func(gen_per_hour, st_hour, prem):
    profit = (gen_per_hour * st_hour) + prem
    return profit


try:
    gph = int(input("Выроботка в час:\n>>"))
except Exception:
    print("Ошибка ввода!!!")

try:
    sth = int(input("ставка в час:\n>>"))
except Exception:
    print("Ошибка ввода!!!")

try:
    prem = int(input("премия:\n>>"))
except Exception:
    print("Ошибка ввода!!!")

print(my_func(gph, sth, prem))
