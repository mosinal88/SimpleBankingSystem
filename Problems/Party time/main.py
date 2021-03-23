guest = []
i = 0
while True:
    name = input()
    if name == '.':
        break
    else:
        guest.append(name)
        i += 1
print(guest)
print(i)
