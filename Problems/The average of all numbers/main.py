# put your python code here
a = int(input())
b = int(input())
i = 0
summa = 0
for s in range(a, b + 1):
    if s % 3 == 0:
        i += 1
        summa += s
print(summa / i)
