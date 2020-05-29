price_of_fruits = {
    'orange' : 100,
    'watermelon' : 200,
    'grapes' : 300
}

#shopkeeper started giving discout on every fruit by 50%
def discount (fruit ,discount = 0.10):
    """
    this function returns price after discount
    """
    discount_rate = discount
    marked_price = price_of_fruits[fruit]

    discount_amount = marked_price *discount_rate
    price = marked_price - discount_amount

    return price

print(discount.__doc__)

print(discount('orange'))

print(discount('orange', 0.30))