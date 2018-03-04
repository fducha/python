import json

data = json.loads(input())
mydata = {}
for row in data:
    mydata[row[u'name']] = row[u'parents']
# print(mydata)

rmydata = {}
for child, parents in mydata.items():
    s = set()
    s.add(child)
    rmydata.setdefault(child, s)
    for p in parents:
        s1 = set()
        s1.add(p)
        rmydata.setdefault(p, s1)
        rmydata[p].add(child)
# print(rmydata)


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


for k, v in sorted(rmydata.items()):
    print(k, ':', len(dfs(rmydata, k)))
