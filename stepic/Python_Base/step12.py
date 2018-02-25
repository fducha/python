ierarhy = {}


def has_relation(parent_class: str, child_class: str) -> bool:
    global ierarhy
    if parent_class not in ierarhy:
        return False
    if child_class not in ierarhy:
        return False
    if parent_class in ierarhy[child_class]:
        return True
    else:
        if len(ierarhy[child_class]) == 0:
            return False
        for cl in ierarhy[child_class]:
            if has_relation(parent_class, cl):
                return True


for i in range(int(input())):
    row = input()
    if ':' in row:
        child, parents = row.split(' : ')
        parents = parents.split(' ')
        ierarhy.setdefault(child, [])
        ierarhy[child].extend(parents)
    else:
        ierarhy.setdefault(row, [])


given_ex, useless_ex = [], []
for i in range(int(input())):
    ex = input()
    if ex in given_ex:
        continue
    if not given_ex:
        given_ex.append(ex)
        continue
    for e in given_ex:
        if has_relation(e, ex):
            useless_ex.append(ex)
            break
    if ex not in useless_ex:
        given_ex.append(ex)


# print(ierarhy)
print(*useless_ex, sep='\n')
print(ZeroDivisionError.mro())
