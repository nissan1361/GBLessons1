

class Date:
    @classmethod
    def transform(cls, date):
        date_transformed = date.split('-')
        new_date_trans = []
        for dat in date_transformed:
            new_date_trans.append(int(dat))
        return new_date_trans


    @staticmethod
    def validate(date):
        if date[0] > 30:
            raise Exception('Не верное число!')
        elif date[0] < 1:
            raise Exception('Не верное число!')
        else:
            print("Число: ", date[0])

        if date[1] > 12 or date[1] < 1:
            raise Exception('Не верный месяц!')
        else:
            print("Месяц: ", date[1])

        if date[2] > 9999:
            raise Exception('Не верно введён год!')
        else:
            print("Год: ", date[2])


years = input("Введите дату чч-мм-гггг\n>>")
some_date = Date.transform(years)
mc = Date()
print(mc.validate(some_date))

