x, y = 0, 0
for i in range(int(input())):
    direction, lenght = input().split()
    lenght = int(lenght)
    if direction == 'восток':
        x += lenght
    elif direction == 'запад':
        x -= lenght
    elif direction == 'север':
        y += lenght
    else:
        y -= lenght

print(x, y)
