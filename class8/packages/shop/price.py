price_of_fruits = {
    'orange' : 100,
    'watermelon' : 200,
    'grapes' : 300,
    'tomato' : 100,
    'potato':120
}

#shopkeeper started giving discout on every fruit by 50%
def discount (my_list ,discount = 0.10):
    """
    this function returns price after discount
    """
    discount_rate = discount
   

    selling_price = {}

    for i in my_list:
        marked_price = price_of_fruits[i]
        discount_amount = marked_price *discount_rate
        price = marked_price - discount_amount
        selling_price[i] = price

    return selling_price
