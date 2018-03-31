from random import randint


class InversionCounter:
    def __init__(self, lst):
        self.lst = lst
        self.counter = 0
        self.sort()

    def _merge(self, lst_l, lst_r):
        result = []
        while len(lst_l) != 0 and len(lst_r) != 0:
            l, r = lst_l[0], lst_r[0]
            if l <= r:
                result.append(l)
                lst_l = lst_l[1:]
                # if l == r:
                #     self.counter -= 1
            else:
                result.append(r)
                lst_r = lst_r[1:]
                self.counter += len(lst_l)
            # self.counter += 1
        if len(lst_l) != 0:
            result.extend(lst_l)
        if len(lst_r) != 0:
            result.extend(lst_r)
        return result

    def sort(self):
        result = []
        for i in self.lst:
            result.append([i])
        while len(result) > 1:
            result.append(self._merge(result.pop(0), result.pop(0)))
        # self.counter = 0
        # self.lst = self._merge(result.pop(0), result.pop(0))

    def __repr__(self):
        return '{}'.format(self.counter)


# a = [7, 2, 5, 3, 7, 13, 1, 6]
# a = [2, 3, 9, 2, 9]
# ic = InversionCounter(a)
# print(ic.lst)
# print(ic)

# n, nums = int(input()), list(map(int, input().split()))
# ic = InversionCounter(nums)


def simple_approach(nums: list) -> int:
    # O(n^2) solution
    counter = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i, n):
            if nums[i] > nums[j]:
                counter += 1
    return counter


def other_approach(nums: list) -> int:
    counter = 0
    # n = len(nums)
    max = 0
    # digits = {}
    for n in nums:
        if n > max:
            max = n
        else:
            counter += 1
        # digits.setdefault(n, 0)
        # digits[n] += 1
        # counter += len(list(filter(lambda x: x > n, digits.keys())))
    return counter


def test():
    n = randint(10, 100)
    # lst = [randint(1, 1000) for _ in range(n)]
    lst = [7, 2, 5, 3, 7, 13, 1, 6]
    # lst = [11, 15, 7, 14]
    # lst = [2, 3, 9, 2, 9]
    print('Original list', *lst)
    print('Simple approach counter = ', simple_approach(lst))
    print('Other approach counter = ', other_approach(lst))
    print('Merge sort approach counter = {}'.format(InversionCounter(lst).counter))


if __name__ == '__main__':
    test()