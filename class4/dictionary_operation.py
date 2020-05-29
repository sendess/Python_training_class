person = {
    'name' : 'John Doe' ,
    'age' : 20,
    'gender' : 'm'
}

print(person)

#inserting
person['country'] = 'Nepal'
person['hobbies'] = ['sports', 'reading']
person['pet_names'] = {
    'cat' : 'oatmeal'
}
print(person)

#retreval
print(person['name'])
print(person.get('surname','not found'))

#deleting key pair vlaue
del person['age']
print(person)

#.items() .keys()  .values()


print(person.items())
print(person.keys())
print(person.values())

#updating a existing key value pair
person['country'] = 'US'
print(person)

for i in person:
    print(i)

for i in person.values():
    print(i)

for i in person.keys():
    print(f'person[{i}]: {person[i]}')

for i in person.items():
    print(f"person[{key}]: {val}")

for key ,val in person.items():
    print(key, val)

