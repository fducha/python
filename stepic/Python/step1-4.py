figure = str(input())

if figure == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif figure == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
elif figure == 'круг':
    a = float(input())
    print(3.14 * (a * a))
