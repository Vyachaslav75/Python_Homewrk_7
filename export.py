def write_file(data):
    with open('phone.txt', 'a', encoding='utf8') as file:
        file.write('\n' + ', '.join(data))
