summa = 0
i = 0
while True:
    number = input()
    if number == '.':
        break
    else:
        summa += int(number)
        i += 1
print(summa / i)
