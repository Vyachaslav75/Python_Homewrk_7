def show_phones(data):
    for i in data:
        print(
            f'ID {i[0]}, Имя: {i[1]}, Фамилия: {i[2]}, Номер телефона: {i[3]}, Коментарий: {i[4]}')


def show_names(data):
    for i in data:
        print(f'Имя: {i[1]}, Фамилия: {i[2]}')


def input_phones():
    res = []
    fields = ['Введите ID, целое число:  ', 'Введите имя:  ', 'Введите фамилию:  ',
              'Введите номер телефона:  ', 'Введите коментарий:  ']
    for i in fields:
        temp = input(i)
        if temp:
            res.append(temp)
        else:
            res.append('-')
    return res
