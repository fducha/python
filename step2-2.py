from fractions import gcd
a, b = int(input()), int(input())
print(int(a * b / gcd(a, b)))
