from time import sleep


def f(x: int) -> int:
    sleep(.45)
    return x + x


result = {}

for i in range(int(input())):
    a = int(input())
    if a not in result:
        result[a] = f(a)
    print(result[a])
