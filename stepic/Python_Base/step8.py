ierarhy = {}


def has_relation(parent, child):
    global ierarhy
    if not ierarhy.get(child):
        return False
    if parent in ierarhy[child]:
        return True
    else:
        for it in ierarhy[child]:
            if has_relation(parent, it):
                return True
    return False


for i in range(int(input())):
    klass = input()
    if ':' in klass:
        child, parents = klass.split(' : ')
        parents = parents.split(' ')
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
