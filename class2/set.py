#set

fruits = {'orange','apple'}
print(fruits,type(fruits))

#empty set

fruits = set()
print(fruits,type(fruits))

fruits={'banana', 'berry', 'apple', 'grape' ,'orange'}
print(fruits)

fruits={'banana', 'berry', 'apple', 'grape' ,'orange','banana'}
print(fruits)

#not accessable
#fruits[0]

#  Are they mutable?
#   yess

#mutable
fruits.add('papaya')
print(fruits)

vegetable = frozenset({'potato','carrot','raddish'})
print(vegetable)

# can add in frozen set
#vegetable.add('ginger')