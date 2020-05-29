import os

print(os.getcwd())
print(os.chdir('D:\Python classes\class 7\os operation'))
print(os.getcwd())

with open('todo.txt','r') as f:
    print(f.read())

os.mkdir('testdir')
os.rmdir('testdir')
#os.remove('remove.xlsx')


#os.walk

for i in os.walk('D:\Python classes'):
    print(i)

print(os.path.join('abc', 'def'))