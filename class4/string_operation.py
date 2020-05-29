text = 'Hello world'
print(text[:5])

for char in text:
    print(char, end=' ')

# .count()
print(text.count('Hello'))


#.split()

print(text.split('l'))

text = input("Enter a string: ")
print(text.split(' '))

#.startswith()/endswith()

print(text.startswith('Hel'))
print(text.startswith('sdl'))

print(text.endswith('ld'))

# repeating strings
print(text * 10)

text = 'Hello world'
# replace sting
print(text.replace('world','people'))

#upper() lower()

print(text.upper())
print(text.lower())

#stri() lstrip() rstrip() used to remove white spaces 

text = '            some text                  '
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# join()

some_arr = ['This', 'Is', 'A','Test','String']
print(' '.join(some_arr))
print('--'.join(some_arr))


text = 'apple'

print('-'.join(text))

#reverse string
text = 'Hello world'
print(text[::-1])