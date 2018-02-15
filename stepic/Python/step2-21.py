from re import split

with open('dataset_3363_2.txt') as f:
    data = f.readline().strip()
    l = split('(\d+)', data)
    print(l)
    for i in range(len(l) - 1):
        if (i % 2) == 0:
            print(l[i] * int(l[i + 1]), end='')
