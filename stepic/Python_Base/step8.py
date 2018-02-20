ierarhy = {}


def add_grandparents(child, fathers):
    for men in fathers:
        if ierarhy.get(men):
            pass


for i in range(int(input())):
    klass = input()
    if ':' in klass:
        child, parents = klass.split(' : ')
        parents = parents.split(' ')
        add_grandparents(child, parents)
        parents.append(child)
    else:
        child, parents = klass, [klass]
    ierarhy[child] = parents

result = []
for i in range(int(input())):
    parent, child = input().split(' ')
    # if has_relation(parent, child):
    #     result.append('Yes')
    # else:
    #     result.append('No')

print(ierarhy)
print(*result, sep='\n')
