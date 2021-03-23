number = int(input())
prime = 1

for i in range(number):
    i += 1
    if i != 1 and i != number and number % i == 0:
        prime = 0

if number > 1 and prime == 1:
    print('This number is prime')
else:
    print('This number is not prime')
