def myFuncUsers():
    userInfo = {
        'name': 'Ваше имя \n>>',
        'surname': 'Ваша фамилия \n>>',
        'birthday': 'Ваш год рождения \n>>',
        'email': 'Ваш Email \n>>'
    }
    user = {}
    for key, value in userInfo.items():
        user[key] = input(value)

    return user


print(myFuncUsers())
