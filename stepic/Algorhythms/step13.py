def merge(lst_l, lst_r):
    max_len = len(lst_l) + len(lst_r)
    result = []
    a, b = lst_l[0], lst_r[0]
    for i in range(max_len):
        if a <= b:
            result.append(a)
            lst_l = lst_l[1:]
        else:
            result.append(b)
            lst_r = lst_r[1:]
        # FIX IT
        a, b = lst_l[0], lst_r[0]
    return result


def merge_sort(lst):
    result = []
    for i in lst:
        result.append([i])
    while len(result) > 1:
        result.append(merge(result.pop(0), result.pop(0)))
    return result


a = [7, 2, 5, 3, 7, 13, 1, 6]
s = merge_sort(a)
print(s)

# n, nums = int(input()), list(map(int, input().split()))

# counter = 0


# O(n^2) solution
# for i in range(n - 1):
#     for j in range(i, n):
#         if nums[i] > nums[j]:
#             counter += 1



# print(counter)