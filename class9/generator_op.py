#generators
#yield

def square(num):
    #return num ** 2
    yield(num ** 2)

print(square(10))

#print(dir(square(10))
test = square(10)
print(next(test))

print('\n\n\n')
#def my_gen(a):
 #   return a
#    a += 1  #does not execute after return is called

#print(my_gen(1))
#print(my_gen(2))

def my_gen():
    a = 0
    print('First')
    yield a

    a += 1
    print('Second')
    yield a 

    a += 1
    print('Third')
    yield a

a = my_gen()
print(next(a))
print(next(a))
print(next(a))

print('\n\n\n')
#print(next(a))   #stopiteration error

#my_gen fucntion returns iterator()

for i in my_gen():
    print(i)


#class object:
#   def next()
#
#   def iter()
print('\n\n\n')
def test():
    a = 0
    while True:
        if a % 2 == 0:
            yield a
        a += 1

temp = test()
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
next(temp)