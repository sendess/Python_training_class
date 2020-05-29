#      Task 3
#      Write a program to print out the frequencies of letters in a USER INPUT string.Write a program to print out the frequencies of letters in a USER INPUT string.

str_to_analyze = input("Enter the string to be analyzed :")  
frequency_list = {} 
for i in str_to_analyze: 
    if i in frequency_list: 
        frequency_list[i] = frequency_list[i] + 1
    else: 
        frequency_list[i] = 1 
print ("frequency of all characters in entered string is :")
dict_of_count = str(frequency_list)
print(dict_of_count)


dict_list=[]
for i,j in dict.iteritems():
    dict_list.append ((i,j))
print (dict_list)