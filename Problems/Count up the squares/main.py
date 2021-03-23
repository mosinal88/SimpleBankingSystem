# put your python code here
summa = 0
squares = 0
while True:
    n = int(input())
    if n == 0 and summa == 0:
        break
    else:
        summa += n
        squares += n ** 2
        if summa == 0:
            break
if squares == 0:
    print(0)
else:
    print(squares)
