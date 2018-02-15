num = int(input())
word = 'программист'

while num != -1:
    if num % 10 == 1 and num % 100 != 11:
        print(num, word)
    elif 1 < num % 10 < 5 and not (11 < num % 100 < 15):
        print(num, word + 'а')
    else:
        print(num, word + 'ов')
    num = int(input())