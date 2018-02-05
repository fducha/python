nums = [int(i) for i in input().split()]
a = int(input())
if a not in nums:
    print('Отсутствует')
else:
    for i in range(len(nums)):
        if nums[i] == a:
            print(i, end=' ')
