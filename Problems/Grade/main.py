user_score = input()
max_score = input()
result = (float(user_score) / float(max_score)) * 100
if 90 <= result <= 100:
    print('A')
elif 80 <= result < 90:
    print('B')
elif 70 <= result < 80:
    print('C')
elif 60 <= result < 70:
    print('D')
elif result < 60:
    print('F')
