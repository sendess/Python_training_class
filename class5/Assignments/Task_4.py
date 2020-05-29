#       Task 4
#       write a function that takes list of numbers as input and returns a new list removing all prime numbers. (try using the same prime function)

entered_list=[]
removed_list=[]

def prime(iter_number, list_given):
    count = 1
    removing_function = lambda m : list_given.append(iter_number) if(m == 0) else ' '
    for i in range(1,iter_number):
        if iter_number % i == 0:
            count += 1
    if count == 2:
        removing_function(1)
    else:
        removing_function(0)

num_entered = int(input("Enter how many numbers do you want to enter: "))
for i in range(num_entered):
    entered_list.append(int(input()))

for j in entered_list:
    prime(j, removed_list)

print("You entered numbers: ")
print(entered_list)

print("After removing prime numbers form the list: ")
print(removed_list)