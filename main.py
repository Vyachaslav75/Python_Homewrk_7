import controller as c
user_choice=0
while user_choice<6:
    print('Программа телефонный справочник')
    print('Если хотите просмотреть контакты полностью нажмите 1')
    print('Если хотите просмотреть имя, фамилию нажмите 2')
    print('Если хотите сортировать контакты по ID нажмите 3')
    print('Если хотите сортировать контакты по имени нажмите 4')
    print('Если хотите добавить контакт нажмите 5')
    print('Если хотите выйти из программы нажмите 6')
    user_choice = int(input('Ваш выбор:  '))
    c.user(user_choice)
