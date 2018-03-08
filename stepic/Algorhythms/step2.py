from random import randint

x, y = 0, 1
# n = randint(1, 10 ** 7)
n = int(input())
# n = 875577
for i in range(2, n + 1):
    ln = (x + y) % 10
    # fib = a + b
    # print('n = {}, a = {}, b = {}, fib = {}, ln = {}'.format(i, a, b, fib, ln), end=' ')
    # if int(str(fib)[-1]) == ln:
    #     print('OK')
    # else:
    #     print('FAIL!!!!!!!!!!!!!!!!!!!!!!!!!!')
    # a, b = b, fib
    x, y = y, ln
    # a, b = b, (a + b) % 10
print(n, ln)
