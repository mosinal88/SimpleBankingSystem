x = int(input())
y = int(input())
if (x == 1 and (y in (1, 8))) or (x == 8 and (y in (1, 8))):
    print(3)
elif (x == 1 and (y != 1 or y != 8)) or (y == 1 and (x != 1 or x != 8)):
    print(5)
elif (x == 8 and (y != 1 or y != 8)) or (y == 8 and (x != 1 or x != 8)):
    print(5)
else:
    print(8)
