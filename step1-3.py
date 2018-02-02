a, b, op = float(input()), float(input()), str(input())

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a / b)
elif op == 'mod':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a % b)
elif op == 'pow':
    print(a ** b)
elif op == 'div':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a // b)
