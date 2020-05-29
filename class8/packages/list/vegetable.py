def add_vegetable(vegetable, my_list):
    f = vegetable
    if f not in my_list:
        my_list.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))
    return my_list

def remove_vegetable(vegetable, my_list):
    f = vegetable
    if f in my_list:
        my_list.remove(f)
        print('{} Removed to list'.format(f))
    else:
        print('{} not in list'.format(f))
    return my_list
    