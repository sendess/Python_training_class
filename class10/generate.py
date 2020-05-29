def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


fibo = fibonacci()
n = int(input('Enter the number of terms: '))
for i in range(1, n+1):
    print(next(fibo))

sq_num = (i ** 2 for i in range(100))
for i in range(10):
    print(next(sq_num))