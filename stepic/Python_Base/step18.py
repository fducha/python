with open('dataset_24465_4.txt') as ifile, open('out.txt', 'w') as ofile:
    data = []
    for row in ifile:
        data.append(row.strip())
    for row in reversed(data):
        ofile.write(row + '\n')
