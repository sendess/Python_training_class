#       Task 4
#       Write a program to merge two dictionaries into one.

dict_1={}
dict_2={}
print("Enter the keys and values for dictionary 1.")
while True:
    key_1 = input("enter the key : ")
    value_1 = input("enter its value : ")
    dict_1[key_1] = value_1
    check = input("Entry for dictionary 1 over? then press 'N'' \t else press enter to continue: ")
    if check == 'n' or check == 'N':
        break
print("Keys and values in dictionary 1:")
print(dict_1)


print("Enter the keys and values for dictionary 2.")
while True:
    key_2 = input("enter the key : ")
    value_2 = input("enter its value : ")
    dict_2[key_2] = value_2
    check = input("Entry for dictionary 2 over? then press 'N'' \t else press enter to continue: ")
    if check == 'n' or check == 'N':
        break
print("Keys and values in dictionary 2:")
print(dict_2)

print("merging the two dictionaries ::")
dict_3 = {**dict_1, **dict_2}
print(dict_3)
