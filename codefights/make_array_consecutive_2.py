def makeArrayConsecutive2(statues):
    counter = 0
    for i in range(min(statues), max(statues)):
        if i not in statues:
            counter += 1
    return counter


print(makeArrayConsecutive2([6, 2, 3, 8]))
print(makeArrayConsecutive2([0, 3]))
print(makeArrayConsecutive2([5, 4, 6]))
print(makeArrayConsecutive2([6, 3]))