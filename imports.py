def read_file():
    res = []
    with open('phone.txt', 'r', encoding='utf8') as file:
        for line in file:
            res.append([x for x in line.rstrip().split(', ')])
    return res

