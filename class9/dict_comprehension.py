a={}
for i in range(5):
    a[i]=i**2
print(a)

#a={key:value for i in ...}
a={i:i**2 for i in range(5)}
print(a)

#dictionary comprehension with if
even={i:i**2 for i in range(10) if i%2==0}

#dictionary with multiple if statement
even={f'this {i}':i**2 for i in range(10) if i%2==0 if i>5}
print (even)

#if else
#[1:'odd',2:'even']
check={}
for i in range(10):
    if i%2==0:
        check[i]='even'
    else:
        check[i]='odd'
print (check)
#comprehension:
check={i:('even' if i%2==0 else 'odd')for i in range(10)}
print(check)

{1:{1:1,2:2},2:{1:1,2:2},3:{}}
numbers={i:{j:j for j in range(2)}for i in range(5)}
print(numbers)

numbers = [{i : j for j in range (2)}for i in range(5)]
print(numbers)


temp = lambda x : x ** 2
test = [temp(i) for i in range(5)]
print(test)

