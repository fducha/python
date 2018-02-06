matrix = []
row = input()
while row != 'end':
    matrix += [[int(i) for i in row.split()]]
    row = input()
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row - 1][col] +
              matrix[(row + 1) % len(matrix)][col] +
              matrix[row][col - 1] +
              matrix[row][(col + 1) % len(matrix[row])],
              end=' ')
    print()
