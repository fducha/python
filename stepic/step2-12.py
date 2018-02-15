count = int(input())
num = 1
while count >= 0:
    if count - num < 0:
        print((str(num) + ' ') * count, end='')
    else:
        print((str(num) + ' ') * num, end='')
    count -= num
    num += 1
