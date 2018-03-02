import json


data = json.loads(input())
mydata = {}
for row in data:
    mydata[row['name']] = row['parents']
print(mydata)
data2 = {}


def parent_plus(class_name, parents):
    global data2
    global mydata
    data2.setdefault(class_name, 1)
    for p in parents:
        data2.setdefault(p, 0)
        data2[p] += 1
        parent_plus(p, mydata[p])


for k, v in mydata.items():
    parent_plus(k, v)

for k in sorted(data2.keys()):
    print(k, data2[k])
