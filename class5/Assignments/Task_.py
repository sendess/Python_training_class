print("Task 3 and Task 4:")
def prime(num,b,d):
    c=1
    nm=num
    fun=lambda n: b.append("prime") if (n==1) else b.append(nm)
    rem=lambda m: d.append(nm) if(m==0) else ' '
    for j in range(1,nm):
        if nm%j == 0:
            c+=1
    if c<=2:
        fun(1) 
        rem(1)
    else:
        fun(0)
        rem(0)
a=[]
p=int(input("Enter how many numbers do you want to enter: "))
for i in range(p):
    a.append(int(input()))
b=[]
d=[]
for k in a:
    prime(k,b,d)
print("You entered: ")
print(a)
print("Replacing prime numbers with 'prime' : ")
print(b)
print("Removing prime numbers:")
print(d)

