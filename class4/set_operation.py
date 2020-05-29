basket = {'orange','apple','grape'}
shelf = {'apple','pear'}

#intersection

print(basket.intersection(shelf))
print(basket & shelf)

#union

print(basket.union(shelf))
print(basket | shelf)

#A-B operation

print(basket.difference(shelf))
print(basket - shelf)

#not (A n B)
print(basket.symmetric_difference(shelf))
print(basket ^ shelf)

#superset and subset
basket = {'apple'}
shelf = {'grape','apple','grape'}

print(basket.issubset(shelf))
print(shelf.issubset(basket))

print(shelf.issuperset(basket))
print(basket.issuperset(shelf))