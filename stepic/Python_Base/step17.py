from itertools import takewhile


def is_prime(x):
    count_div = 0
    for i in range(x + 1):
        if i != 0 and x % i == 0:
            count_div += 1
    return count_div == 2


def primes():
    num = 1
    while True:
        num += 1
        if is_prime(num):
            yield num


# a = []
# for i in range(31):
#     if is_prime(i):
#         a.append(i)
#
# print(a)

print(list(takewhile(lambda x: x <= 31, primes())))
