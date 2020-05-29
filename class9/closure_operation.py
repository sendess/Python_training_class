#higher order component

def display(to_display):
    def inner_function():
        print('this is the value to print:  ',to_display)
    return inner_function


#closure
lets_display = display('Hello World')
lets_display()

#normal function

def normal_function(b):
    a = 2
    print(a)

#normal_function('abcd')
#print(b)