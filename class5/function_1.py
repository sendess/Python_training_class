# function wihout positional argurments/parameters

list_to_buy = []
def add_orange():
    orange = 'orange'
    if orange not in list_to_buy:
        list_to_buy.append(orange)
        print('{} added to the list'.format(orange))
    else:
        print('{} already in list'.format(orange))

add_orange()
add_orange()
print(list_to_buy)


def add_watermelon():
    watermelon = 'watermelon'
    if watermelon not in list_to_buy:
        list_to_buy.append(watermelon)
        print('{} added to the list'.format(watermelon))
    else:
        print('{} already in list'.format(watermelon))
add_watermelon()
add_watermelon()
print(list_to_buy)

def remove_orange():    
    orange='orange'
    if orange in list_to_buy:
        list_to_buy.remove(orange)
        print('{} added to list'.format(orange))
    else:
        print('{} already in list'.format(orange))
add_orange()
add_orange()
add_watermelon()
remove_orange()
print(list_to_buy)