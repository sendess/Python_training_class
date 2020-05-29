with open('first.txt', 'rb+') as f:
    message ='Hello world'
    f.write(message)
    print(message.decode('ASCII'))
    print(f.read())
