# type conversions implicit and explicit

a = 5
b = 2.12
c = a + b

print('type of a: ',type(a))
print('type of b: ',type(b))
print('type of c: ',type(c))


a = '123'
b = 1

print(a,'type of a: ',type(a))
print('sum = ', int(a) +b )

print(int('1010', 2))
print(int('12', 8))

print(type(str(123)))
float(123)
int(3.1415)
print(set([1, 2, 3, 3, 2]))
print(dict([('abc',1),('def',2)]))
print(list('abcdefg'))
print(tuple([1, 2, 3, 4]))

a = 2
if(a < 5):
    pass  #used when nothing is to be done, used rather than empty statement which throws error

for i in range(10):
    print(i)
else:
    print('fully executed!!')

for o in range(10):
    print(o)
    if o == 4 :
        break
else:
    print('fully executed!!')


a = 10
while a > 0:
    print(a)
    a -= 1
else:
    print('fully execute')

print(list(range(10, -9, -2)))

