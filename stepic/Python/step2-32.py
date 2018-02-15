with open('dataset_3380_5.txt') as file:
    heights = {}
    for row in file:
        datas = row.split('\t')
        klass = int(datas[0].strip())
        heights.setdefault(klass, [])
        heights[klass].append(int(datas[2].strip()))

    for kl in range(1, 12):
        if kl in heights:
            print(kl, sum(heights[kl]) / len(heights[kl]))
        else:
            print(kl, '-')
