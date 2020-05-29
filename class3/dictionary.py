fruits = ['orange','watermelon','grapes','mango','apple']
price = [100, 120, 90, 230, 200]

#fruits          |   price
#__________________________
#orange          |   100
#watermelon      |   120
#grapes          |   90
#mango           |   230
#apple           |   200


#empty dictionary
price_of_fruits = {}
print(price_of_fruits,type(price_of_fruits))

#empty dictionary
price_of_fruits = dict()
print(price_of_fruits,type(price_of_fruits))

price_of_fruits = {
    'orange' : 100,
    'watermelon' : 120,
    'grapes' : 90,
    'mango' : 230,
    'apple' : 200
}
print(price_of_fruits)

orange_price = price_of_fruits['orange']
print(orange_price)

appple_price = price_of_fruits.get('apple')
print(appple_price)

#fruits          |   Min price      |   Min price
#___________________________________________________
#orange          |   100            |   120
#watermelon      |   120            |   340
#grapes          |   90             |   110
#mango           |   230            |   250
#apple           |   200            |   220


min_max_price = {
    'orange' : [100, 120],
    'watermelon' : [120, 340],
    'grapes' : [90, 110],
    'mango' : [230, 250],
    'apple' : [200, 220]
}

print(min_max_price)

keys = min_max_price.keys()
values = min_max_price.values()

print(keys,values)

min_max_price['mango'] = [130,150]
print(min_max_price)