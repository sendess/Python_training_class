#higher order funciton

test_list = list(range(14))

def function(x):
    return x * x

    
print(list(map(function, test_list)))
def my_map(f, list_sent):
    new_list = []
    for i in list_sent:
        new_list.append(f(i))
    return new_list

print(my_map(function,test_list))

def is_even(x):
    if x % 2 == 0:
        return True
    return False

print(list(filter(is_even,test_list)))


print(list(filter(lambda x: not is_even(x),test_list)))

def my_filter(f, l):
    new_list = []
    for i in l:
        if f(i):
            new_list.append(i)
    return new_list

print(my_filter(is_even, test_list))

def odd_even(n):
    def odd():
        return 'you are odd bro'
        
    def even():
        return 'we all are even here'

    if n % 2 == 0:      
        return even
    return odd

fun = odd_even(10)
print(fun)