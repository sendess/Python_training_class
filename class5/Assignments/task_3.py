#       Task 3
#       Replace prime numbers with 'prime' string in a given list of integers using lambda function. (you can use separate function to check for prime)

entered_list=[]
replaced_list=[]

def prime(iter_number, list_given):
    count = 1
    changing_function = lambda n : list_given.append('Prime') if (n==1) else list_given.append(iter_number)
    for i in range(1,iter_number):
        if iter_number % i == 0:
            count += 1
    if count == 2 :
        changing_function(1) 
    else:
        changing_function(0)

num_entered = int(input("Enter how many numbers do you want to enter: "))
for i in range(num_entered):
    entered_list.append(int(input()))   

for j in entered_list:
    prime(j, replaced_list)

print("You entered numbers: ")
print(entered_list)

print("Replacing prime numbers in the list with 'Prime' : ")
print(replaced_list)
