number=int(input('Check natural number till? :'))
test_list=range(1, number)
def is_prime(n):
    if n==0 or n==1:
        return n
    for i in range(2,n):
        if n%i==0:
            return n
    return 'prime'
prime=lambda n:'prime' if list(is_prime(n)) else n
print(list(map(is_prime,test_list)))


