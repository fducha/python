def binary_search(k: int, lst: list) -> int:
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] == k:
            return m + 1
        elif lst[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


n_nums = list(map(int, input().split()))[1:]
k_nums = list(map(int, input().split()))[1:]

for i in k_nums:
    print(binary_search(i, n_nums), end=' ')
