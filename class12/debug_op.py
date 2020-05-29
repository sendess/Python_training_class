import pdb
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
@dash
@check_even
def display(a):
    print(a)

pdb.set_trace()
display(2, 23, 4, 2)

print('Hello')
for i in range(10):
    print('test')
#display(45)
#display(44)

'''
l
n               single line execution
c               returns to continous flow
b               lists all the breakpoint
b line number   breakpoint at certain line
cl              removes all breakpoint
cl line number  removes breakpoint at specfic line
p               
'''