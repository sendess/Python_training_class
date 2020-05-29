days = ['Sunday', 'Moday', 'Tuesday']

#append() for adding one value to list at a time

days.append('Wednesday')
print(days)

days.append('Thursday')
print(days)

#extend() for adding multiple values to a list at a time

days.extend(['Friday','Saturday'])
print(days)

# insert() to add in between elements
days.insert(1,'random day')
print(days)
days.insert(6,'random day')
print(days)

days = days[:3] + ['random day 2', 'random day 3'] + days[3:]
print(days)

#remove()
days.remove('random day 3')
days.remove('random day 2')
days.remove('random day')
days.remove('random day')
print(days)

#pop()
#days.pop(1)
print(days.pop(1))
print(days)

#sort()
days.sort()
print(days)
some_arr = [10,123,123,324,534]
some_arr.sort()
print(some_arr)

#reversal()
print(days[::-1])


#list and tuple unpacking

days = ['Sunday', 'Moday', 'Tuesday']
sun, mon, tue = days
print(sun, mon, tue)

days = tuple(days)
sun, mon, tue = days
print(sun, mon, tue)

print('saturday' in days)
print('Sunday' in days)

#for which in C we should have to do this looping
#for day in days:
#    if day == 'saturday':
#        print(True)