# function wih positional argurments/parameters
list_fruits=[]
def add_fruit(fruit):
    f=fruit
    if f not in list_fruits:
        list_fruits.append(f)
        print('{} added to list'.format(f))
    else:
        print('{} already in list'.format(f))

def remove_fruit(fruit):
    f=fruit
    if f  in list_fruits:
        list_fruits.remove(f)
        print('{} removed from list'.format(f))
    else:
        print('{} not in list'.format(f))

fruit = add_fruit

print(fruit)

fruit('Tasdingo')

add_fruit('orange')
add_fruit('apple')
add_fruit('banana')
remove_fruit('orange')
print(list_fruits)