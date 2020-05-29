#I will create a list of fruits to buy
#I will go to market and see discout price

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

price_of_fruits = {
    'orange' : 100,
    'watermelon' : 200,
    'grapes' : 300
}

#shopkeeper started giving discout on every fruit by 50%
def discount (my_list ,discount = 0.10):
    """
    this function returns price after discount
    """
    discount_rate = discount
   

    selling_price = {}

    for i in my_list:
        marked_price = price_of_fruits[i]
        discount_amount = marked_price *discount_rate
        price = marked_price - discount_amount
        selling_price[i] = price

    return selling_price


#lets start
list_to_buy = []
add_fruit('orange', list_to_buy)
add_fruit('watermelon', list_to_buy)
add_fruit('grapes', list_to_buy)
remove_fruit('watermelon', list_to_buy)


print(discount(list_to_buy))

