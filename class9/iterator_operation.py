#iterator and iterable


#this is iterable
i = [1, 2, 3, 4, 5]
#next [i]

print(dir(i))


#this is iterator
i_iterator = i.__iter__()
i_iterator = iter(i)
print('\n\n\n\n')
print(dir(i_iterator))


# all iterable objects can produce ,
# iterator object but they itself are not an iterator
print(next(i_iterator))
print(next(i_iterator))
print(i_iterator.__next__())
print(i_iterator.__next__())
print(i_iterator.__next__())
#print(i_iterator.__next__())  #gives stop iterator error message


#while until we get stop iteration error
for temp in i:
    print(temp)

#for i in range(10):
