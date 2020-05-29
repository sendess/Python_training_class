#       Task 5
#       Adding by sliding list and sum of sum  of elements

def add_by_sliding(l1, l2): 
    i = sum = 0
    diff = len(l1) - len(l2)
    while i <= diff:
        combine = zip(l1, l2)
        for j, k in combine:
            sum = sum + j + k
        del l1[0]    #removing element of list 1 so that addition of 2nd list element again from loop to remaining ones
        i = i + 1
    print("Output after sliding the list_2 over list_1 by following specified addition rule: ", sum)
    
print("Enter list where list 1 is the longer one:\n")
list_1 = []
n1 = int(input("\n\n Enter number of elements in list 1: ")) 
for i in range(0, n1): 
    text_entered = int(input('enter the {}th element of the list 1:'.format(i+1)))
    list_1.append(text_entered)

list_2 = []
n2 = int(input("\n\n Enter number of elements in list 2: ")) 
for i in range(0, n2): 
    text_entered = int(input('enter the {}th element of the list 2:'.format(i+1)))
    list_2.append(text_entered)


if n1 > n2:
    add_by_sliding(list_1, list_2)
else:
    print("Warning!!:----\nPlease enter the 1st list to be longer than 2nd list. ")