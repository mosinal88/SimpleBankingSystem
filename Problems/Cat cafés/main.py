cafe = []
cat = []
maximum = 0
i = 0
while True:
    name = input()
    if name == 'MEOW':
        break
    else:
        cafe_temp = name.split()
        cafe.append(cafe_temp[0])
        cat.append(int(cafe_temp[1]))
for i in cat:
    maximum = cat[0]
    if i >= maximum:
        maximum = i
print(cafe[cat.index(maximum)])
