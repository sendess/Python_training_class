print(__name__)


def add_fruit(fruit, my_list):
    f = fruit
    if f not in my_list:
        my_list.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))
    return my_list


def remove_fruit(fruit, my_list):
    f = fruit
    if f in my_list:
        my_list.remove(f)
        print('{} Removed to list'.format(f))
    else:
        print('{} not in list'.format(f))
    return my_list


def this_is_fruit():
    return __name__


if __name__ == '__main__':
    print(this_is_fruit())
