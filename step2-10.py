nums = [int(i) for i in input().split()]
for i in set(nums):
    if nums.count(i) > 1:
        print(i, end=' ')
