timezone = int(input())
if -12 <= timezone <= 14:
    if timezone + 10.5 < 0:
        print('Monday')
    elif timezone + 10.5 > 24:
        print('Wednesday')
    else:
        print('Tuesday')
