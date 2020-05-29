#Task 1
sum = 0
for i in range(1,1000):
    if  i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print(sum)

#Task 2
sum_sq = 0
sq_sum = 0
difference = 0
for i in range(1,101):
    sum_sq += i ** 2
    sq_sum += i
sq_sum = sq_sum ** 2
difference = sq_sum - sum_sq
print(difference)

#Task 3
number = 2 ** 1000
sum_of_digits = 0
while number != 0:
    sum_of_digits = sum_of_digits + number % 10
    number = number // 10
print(sum_of_digits)