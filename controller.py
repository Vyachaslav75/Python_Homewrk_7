import export as ex
import imports as im
import show


def sort_key(list):
    return list[1]


def sort_key1(list):
    return int(list[0])


def sort_phones(data, flag):
    if flag == 1:
        show.show_phones(sorted(data, key=sort_key1))
    elif flag == 2:
        show.show_phones(sorted(data, key=sort_key))


def user(choice):
    if choice == 1:
        show.show_phones(im.read_file())
    elif choice == 2:
        show.show_names(im.read_file())
    elif choice == 3:
        sort_phones(im.read_file(), 1)
    elif choice == 4:
        sort_phones(im.read_file(), 2)
    elif choice == 5:
        ex.write_file(show.input_phones())
