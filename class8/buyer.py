# lets start#modular
#import fruits
#import price
import sys
#           if need to import specific item(function) from file use keyword from

#from fruits import add_fruit, remove_fruit
#from price import discount


#           after using from "file" import no need to specify file.function(arguement) just function(arguements)

#           absolute and relative path
# Either
#       import packages.list.fruits
# or

# relative import ko tarikaa
#from packages.list.fruits import add_fruit, remove_fruit

#from packages.list.vegetable import add_vegetable, remove_vegetable
from packages.shop.price import discount
# from packages.list import *  #import from __init__
from packages.list.fruits import add_fruit, remove_fruit, this_is_fruit
from packages.list.vegetable import add_vegetable, remove_vegetable
from packages import shop
print(dir())
print(sys.path)
print(__name__)
print(this_is_fruit())
list_to_buy = []
add_fruit('orange', list_to_buy)
add_fruit('watermelon', list_to_buy)
add_fruit('grapes', list_to_buy)
#remove_fruit('watermelon', list_to_buy)
add_vegetable('tomato', list_to_buy)
add_vegetable('potato', list_to_buy)
print(discount(list_to_buy))

