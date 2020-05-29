def decorator_fun(func):
    def inner_fun(a):
        print('Function is decorated')
        func(a)
    return inner_fun
def display(a):
    print(a)

display(7)

decorated = decorator_fun(display)
decorated(4)
def dash(func):
    def inner_func(*args, **kwargs):
        print('--' * 20)
        func(*args,**kwargs)
        print('--' * 20)
    return inner_func
decorated = decorator_fun(display)
decorated(4)




def check_even(fun):
    def inner_func(*args, **kwargs):
        
        for i in args:
            if i % 2 == 0:
                fun('Even')
            else:
                fun('odd')
    return inner_func

check = check_even(display)
check(2)
check(3)
check(2, 23 ,42)
#@check_name

@check_even
def display(a):
    print(a)

display(45)
display(44) 