import csv, operator

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    crimes = {}
    for row in reader:
        if row[2] == 'Date' or row[2].split()[0].split('/')[2] != '2015':
            continue
        crimes.setdefault(row[5], 0)
        crimes[row[5]] += 1
    print(max(crimes.items(), key=operator.itemgetter(1))[0])
