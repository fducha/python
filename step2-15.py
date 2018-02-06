num = int(input())
matrix = [[0 for i in range(num)] for j in range(num)]
value = 0
n = num
offset = 0
while n > 0:
    # up side
    for i in range(n):
        value += 1
        matrix[offset][i + offset] = value
        print(value, end='\t')
    print()
    # right side
    for i in range(n - 1):
        value += 1
        matrix[i + offset + 1][num - offset - 1] = value
        print(value, end='\t')
    print()
    # bottom side
    for i in range(n - 2, -1, -1):
        value += 1
        # matrix[num - 1 - offset][i + 1] = value
        print(value, end='\t')
    print()
    # left side
    for i in range(n - 2, 0, -1):
        value += 1
        # matrix[i][offset] = value
        print(value, end='\t')
    print()
    n -= 2
    offset += 1

for row in matrix:
    [print(i, end='\t') for i in row]
    print()
