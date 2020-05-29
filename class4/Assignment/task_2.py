#     Task 2
#     Write a Python program to remove duplicates from a list

list_before = []
text_entered = input("enter the elements of the list:")
list_before = list(text_entered)
print("Elements of the list before removing replicates: ")
print(list_before)
list_after =list(dict.fromkeys(list_before))
print("Elements of the list after removing replicates:")
print(list_after)
