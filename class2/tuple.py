
##   tuple aka contant list


# begin  tuple
#empty tuple
fruits = tuple()
print(fruits,type(fruits))

#empty tuple
fruits = tuple()
print(fruits,type(fruits))

#define tuple of fruits
fruits = ('banana', 'berry', 'apple', 'grape' ,'orange')
print(fruits,tuple(fruits))

banana = fruits[0]
orange = fruits[4]
grape = fruits[3]

print(banana, orange, grape)

#slicing
summer_fruits = fruits [0:3]
print(summer_fruits)

winter_fruits = fruits [3:]
print(winter_fruits)

#immutable
#fruits[3] = 'Watermelon'
#print(fruits)

print(fruits[-1]) #-1 for last element

print(len(fruits))

