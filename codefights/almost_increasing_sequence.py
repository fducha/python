def almostIncreasingSequence(sequence):
    # count = 0
    # for i in range(len(sequence) - 1):
    #     if sequence[i] >= sequence[i + 1]:
    #         count += 1
    #         if i + 1 < len(sequence) - 1:
    #             if sequence[i] >= sequence[i + 2] and i != 0:
    #                 count += 1
    #     if count > 1:
    #         break
    # return count <= 1
    if len(sequence) <= 2:
        return True
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i - 1] >= sequence[i]:
            if sequence[i] >= sequence[i + 1]:
                count += 1
        if count > 1:
            return False
    return True


print(almostIncreasingSequence([1, 3, 2, 1])) # false
print(almostIncreasingSequence([1, 2, 1, 2])) # false
print(almostIncreasingSequence([40, 50, 60, 10, 20, 30])) # false
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5])) # True
print(almostIncreasingSequence([1, 2, 5, 3, 5])) # True
