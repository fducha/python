def fib(n):
    """Вычисляет n-e число Фибоначи"""

    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_mod(n, m):
    """
    Вычисляет останок от деления n-го числа Фибоначи на m
    Для вычислений используется метод поиска периода Пизано
    """

    k = 0
    s = [0, 1]
    for i in range(2, 6 * m):
        s.append((s[-1] + s[-2]) % m)
        k += 1
        if s[-1] == 1 and s[-2] == 0:
            break
    if k == 0:
        return n % m
    else:
        return s[n % k]
