
# function --->  pass by value /reference
def add_fruit(fruit, my_list, price):

    f = fruit
    print(
        'f {} p {} l {}'.format(id(fruit), id(price), id(my_list)))

    price = 200

    print(
        'f {} p {} l {}'.format(id(fruit), id(price), id(my_list)))
    if f not in my_list:
        my_list.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))
list_to_buy = []

print(
        'p {} l {}'.format(id(price), id(list_to_buy)))
price = 100


print(
        'p {} l {}'.format(id(price), id(list_to_buy)))
        
add_fruit('orange', list_to_buy, price)
print(list_to_buy, price)