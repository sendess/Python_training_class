##   list
##   tuple
##   set
##   dictionary

# begin  list
#empty list
fruits = []
print(fruits,type(fruits))

#empty list
fruits = list()
print(fruits,type(fruits))

#define list of fruits
fruits = ['banana', 'berry', 'apple', 'grape' ,'orange']
print(fruits,type(fruits))

banana = fruits[0]
orange = fruits[4]
grape = fruits[3]

print(banana, orange, grape)

#slicing
summer_fruits = fruits [0:3]
print(summer_fruits)

winter_fruits = fruits [3:]
print(winter_fruits)

#changing/replace item of a list
fruits[3] = 'Watermelon'
print(fruits)

print(fruits[-1]) #-1 for last element

print(len(fruits))

