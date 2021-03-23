number_list = []
while True:
    number = input()
    if number == '.':
        break
    else:
        number = float(number)
        number_list.append(number)
min_number = number_list[0]
for i in number_list:
    if i < min_number:
        min_number = i
print(min_number)
