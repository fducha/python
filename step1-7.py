num = list(map(int, list(str(input()))))
if (sum(num[:3]) == sum(num[3:])):
    print('Счастливый')
else:
    print('Обычный')
