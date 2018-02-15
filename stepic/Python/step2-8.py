nums = [int(i) for i in input().split()]
if len(nums) == 1:
    print(*nums)
else:
    for i in range(len(nums)):
        print(nums[i - 1] + nums[(i + 1) % len(nums)], end=' ')
