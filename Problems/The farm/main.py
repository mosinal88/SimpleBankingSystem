money = int(input())
if 23 <= money < 678:
    if money // 23 > 1:
        print(money // 23, "chickens")
    else:
        print(money // 23, "chicken")
elif 678 <= money < 1296:
    if money // 678 > 1:
        print(money // 678, "goats")
    else:
        print(money // 678, "goat")
elif 1296 <= money < 3848:
    if money // 1296 > 1:
        print(money // 1296, "pigs")
    else:
        print(money // 1296, "pig")
elif 3848 <= money < 6769:
    if money // 3848 > 1:
        print(money // 3848, "cows")
    else:
        print(money // 3848, "cow")
elif money >= 6769:
    if money // 6769 > 1:
        print(money // 6769, "sheep")
    else:
        print(money // 6769, "sheep")
else:
    print("None")
