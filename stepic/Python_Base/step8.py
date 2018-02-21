ierarhy = {}


def has_relation(parent_class: str, child_class: str) -> bool:
    global ierarhy
    if parent_class not in ierarhy:
        return False
    if child_class not in ierarhy:
        return False
    if parent_class == child_class:
        return True
    if child_class in ierarhy[parent_class]:
        return True
    else:
        if len(ierarhy[parent_class]) == 0:
            return False
        for cl in ierarhy[parent_class]:
            if has_relation(cl, child_class):
                return True


for i in range(int(input())):
    klass = input()
    if ':' in klass:
        child, parents = klass.split(' : ')
        parents = parents.split(' ')
        ierarhy.setdefault(child, [])
        for p in parents:
            ierarhy.setdefault(p, [])
            ierarhy[p].append(child)
    else:
        ierarhy.setdefault(klass, [])


result = []
for i in range(int(input())):
    parent, child = input().split(' ')
    # if has_relation(parent, child):
    #     result.append('Yes')
    # else:
    #     result.append('No')
    result.append('Yes' if has_relation(parent, child) else 'No')

print(ierarhy)
print(*result, sep='\n')
