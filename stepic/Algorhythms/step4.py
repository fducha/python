# def gcd(a, b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     if a >= b:
#         return gcd(a % b, b)
#     else:
#         return gcd(a, b % a)


def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()