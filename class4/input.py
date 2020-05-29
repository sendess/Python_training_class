a = input()
print(a,type(a))


#type casting

a = int(input("Enter a number :"))
print(a,type(a))


# output
#sting formatting
weekday = 'Monday'
text = 'Today is ' + weekday
print(text)


text = 'one ' + 'two' + 'three'
print(text)

text = '{} two {}'.format('one','two')
print(text)

text = '{1} two {0}'.format('one','two')
print(text)

#using f-string

text = f'Today is {weekday}'
print(text)
one = 1
two = 2
text = f"{one} two {two}"
print(text)

#using in print statement

print('today is ',weekday)
print(f'Todau is {weekday}')

one = 1.1231241
two = 2
text = f"{round(one,2)} two{two}"
print(text)