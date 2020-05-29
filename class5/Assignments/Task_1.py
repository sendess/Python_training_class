#       Task 1
#       Write a function to generate following pattern that takes number of rows as parameter (default to 5)

def pattern_generate(value = 5):
    for i in range(0, value + 1):
        for j in range (0, i):
            print('*', end = '')
        print()

print('without passing any arguements : \n')
pattern_generate()

input_value = int(input('\n Enter the number of rows required in pattern : '))

pattern_generate(input_value)

