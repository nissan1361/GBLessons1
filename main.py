first_Variable = "Hello GB!"
print(first_Variable)
variable_int = 12
variable_float = 12.0001
user_name = input("Ваше имя: \n >>>")
age = input("Ваш возраст: \n >>>")
print("Hello, {} {}!".format(user_name, age))

if int(age) > 18:
    print("age>18")
elif int(age) > 16:
    print("age>16")
else:
    print("less16")

id = 0
while id < 10:
    print(id)
    id = id+1
