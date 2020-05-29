'''
mode:
r
w
a
b
'''
filehandler = open('first.txt', 'w')
filehandler.write('Hello people')
filehandler.close



filehandler_1 = open('first.txt', 'r')
print(filehandler_1.read())
filehandler_1.close

temp = ['first line\n', 'second line\n', 'third line\n']
filehandler = open('first.txt', 'w')
filehandler.write('Hello people\n second line \n third line\n')
filehandler.writelines(temp)
filehandler.close

filehandler = open('first.txt', 'r')
print(filehandler.read()) # reads whole fiel at once
filehandler.close()


#or read line by line with loop

filehandler = open('first.txt', 'r')
for i in filehandler:
    print(i)
filehandler.close()


filehandler = open('first.txt', 'r')
print(filehandler.readline())
print(filehandler.readline())
filehandler.close()

#try:
#    filehandler = open('first.txt','r')
#final:

with open('first.txt','r+')as filehandler: #file crash hola vvanera
    print(filehandler.read())
    filehandler.write('heyyyyy')

with open('first.txt','r+')as filehandler: 
    print(filehandler.read(4),end = '')
    print(filehandler.read(1))
    print(filehandler.read(2))

    print('the cursor is a: ',filehandler.tell())
    filehandler.seek(0)
    print(filehandler.read())

    filehandler.seek(4)
    print(filehandler.read(6))
filehandler.close()


'''
encoding
windows  cp1252
linux    UTF-8
mac      UTF-8 UTF-16
'''
with open('first.txt','r', encoding = 'cp1252')as f:
    print(f.encoding)