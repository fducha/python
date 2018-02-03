gen = input().lower()
start = 0
while True:
    pattern = gen[start]
    count = 1
    for j in gen[start + 1:]:
        if pattern == j:
            count += 1;
        else:
            start = gen.index(j, start)
            break
    print(pattern, count, sep='', end='')
