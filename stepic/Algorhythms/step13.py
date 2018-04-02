from random import randint


class InversionCounter:
    def __init__(self, lst):
        self.lst = lst
        self.counter = 0
        self.merge_sort(self.lst)

    def _merge(self, lst_l, lst_r):
        result = []
        li, rj = 0, 0
        for _ in range(len(lst_l) + len(lst_r)):
            if rj == len(lst_r) or (li < len(lst_l) and lst_l[li] <= lst_r[rj]):
                result.append(lst_l[li])
                li += 1
            else:
                self.counter += len(lst_l) - li
                result.append(lst_r[rj])
                rj += 1
        return result

    def merge_sort(self, lst: list) -> list:
        n = len(lst)
        if n == 1:
            return lst
        m = n // 2
        return self._merge(self.merge_sort(lst[0:m]), self.merge_sort(lst[m:]))

    def __repr__(self):
        return '{}'.format(self.counter)


def simple_approach(nums: list) -> int:
    # O(n^2) solution
    counter = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i, n):
            if nums[i] > nums[j]:
                counter += 1
    return counter


def test():
    n = randint(10, 100)
    lst = [randint(1, 1000) for _ in range(n)]
    # lst = [14, 8, 2, 4, 3, 9, 0, 11]
    # lst = [11, 15, 7, 14]
    # lst = [2, 3, 9, 2, 9]
    print('Original list', *lst)
    print('Simple approach counter = ', simple_approach(lst))
    print('Merge sort approach counter = {}'.format(InversionCounter(lst).counter))


if __name__ == '__main__':
    # test()
    n, nums = int(input()), list(map(int, input().split()))
    print(InversionCounter(nums))
