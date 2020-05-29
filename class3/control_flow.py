2 == 2
2 == 3
a = 4
b = 5
a == b
a > b
a < b
2 == 2 and 3 == 3
2 == 3 and 3 == 3
2 == 3 or 3 == 3
not True
not False
1 == 1 and 2 == 2 and 3 == 3 and 4 == 4
2 == 2 or 3 == 3 or 4 == 2
2 == 2 or print('executed')
2 == 1 or print('executed')
1 == 1 and 2 == 2 and 3 == 3 and print('and executed')
1 == 1 and 2 == 5 and 3 == 3 and print('and executed')

if True:
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')


if False:
    print('bye world')
    print('bye world')
    print('bye world')
    print('bye world')
    print('bye world')

a = 1
b = 3

if a>b and print('condition is checked!!'):
    print('it is true')
else:
    print('not true')


a = 5
b = 5
if a > b :
    print('it is true')
elif a == b:
    print('both are equal')
elif a == 4:
    print('a is 4')
else :
    print('Nah!!')


if a == b:
    print('equal')
else:
    if a > b:
        print('a is greater')
    else:
        print('b is greater')

#while loop and for loop

#while
c = 10
while(c > 0):
    print('test')
    c = c-1

n = 2
while (True):
    n = n * 2
    c = c + 1
    if n == 1024:
        print('power reached',c)
        break

n = 2
while (True):
    n = n * 2
    c = c + 1
    if n > 999999999999:
        print('power reached',c)
        break

a = 5
while a > 0:
    print(a)
    if a == 2:
        break
    a = a - 1


#continue

a = 10
while a > 0:
    if a%2 != 0:
        a = a - 1
        continue
    print(a)
    a = a - 1

#range(start, end, step)


a = [1,2,3,4,5]
a = ['ram', 'hari', 'me', 'sam']
for i in a:
    print(i,end = ' ')

for i in range(6):
    print (i)

for i in range(5):
    for j in range(5):
        print(i,j)

persons = ['ram', 'hari', 'me', 'sam']
for index, person in enumerate(persons):
    print(index, person)


#fizz buzz


#for i in range(1,50):
#    if i % 5 == 0 and i % 3 == 0:
#        print('fizz buzz')
#    elif i % 3 == 0:
#        print('fizz')
#    elif i % 5 == 0:
#        print('buzz')
#    else:
#        print(i)


for i in range(1,50):
    output = ''
    if i % 3 == 0:
        output = output + 'fizz'
    if i % 5 == 0:
        output = output + 'buzz'
    if output == '':
        output = i
    print(output)


person = {'name':'Shyam', 'age' : 10, 'address':'Rampur'}

for i in person:
    print(i, end = ': ')
    print(person[i])


a = 10  #memory
b = 10  #memory
c = d = 2
print (a is b)
print('id of a:',id(a))
print('id of b:',id(b))

print (c is d)
print('id of c:',id(c))
print('id of d:',id(d))