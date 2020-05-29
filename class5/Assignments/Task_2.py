#       Task 2
#       Write a function to covert following list of tuples into dictionary. 


def change(page_dummy, dict_dummy):
    for i, j in page_dummy:
        dict_dummy.setdefault(i,[]).append(j)
    return dict_dummy
price = [('orange', 100), ('watermelon', 200), ('papaya', 300)]
dict_1 = {}
print("The newly made dictionary:: ")
print(change(price, dict_1))