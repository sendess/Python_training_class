def function(x):
    return x

print(function)

fun = lambda x : x
print(fun)

# or


print(lambda x : x)

def func(x, y, z):
    return x, y, z
print(func)

funct = lambda x, y, z : (x, y, z)
print(funct(*[1, 2, 3]))

l = list(range(10))

square = lambda x : x * x

list(map(square, l))
#or short

list(map(lambda x : x * x, l))
#or even shorter


list(map(lambda x : x * x, list(range(10))))



#fizz buzzzz

#if (x%3 == 0 and x%5 == 0):
#    fizzbuzz
#elif(x%3 == 0):
#    fizzbuzz
#elif(x%5 == 0):
#    buzz

fizzbuzz = lambda x : 'fizzbuzz' if (x % 3 == 0 and x % 5 == 0) else \
    ('fizz' if x % 3 == 0 else ('buzz' if x % 5 == 0 else x))
l = list(range(16))
print(list(map(fizzbuzz, l)))

# Immediately invoked function IIFE

var = lambda x : x * x
var(1)

print((lambda x : x * x)(5))