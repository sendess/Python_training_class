#       Task 1
#       Write a Python program that takes two lists and prints True if they have at least one common member.

list_1 = []
n = int(input("\n\n Enter number of elements in list 1: ")) 
for i in range(0, n): 
    text_entered = input('enter the {}th element of the list 1:'.format(i+1))
    list_1.append(text_entered)



list_2 = []
n = int(input("\n\n Enter number of elements in list 2: ")) 
for i in range(0, n): 
    text_entered = input('enter the {}th element of the list 2:'.format(i+1))
    list_2.append(text_entered)

print("\n\n\nElements of list 1: ")
print(list_1)

print("Elements of list 2: ")
print(list_2)

print("The intersection of two entered lists is: ")
intersect = set(list_1).intersection(list_2)


if not intersect:
    print("\n\n False")
else:
    print("\n\n True")