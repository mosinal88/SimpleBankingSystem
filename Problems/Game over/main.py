scores = input().split()
# put your python code here
correct = 0
errors = 0
for i in scores:
    if i == "C":
        correct += 1
    elif i == "I":
        errors += 1
        if errors == 3:
            break
if errors == 3:
    print('Game over')
    print(correct)
else:
    print('You won')
    print(correct)
