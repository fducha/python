def gen(num):
    s = 0
    i = 0
    while s < num:
        i += 1
        s += i
        yield i


n = int(input())

# summands = [x for x in range(1, n + 1) if n >= sum(range(1, x))]
# print(s)

summands = []
for i in gen(n):
    summands.append(i)
r = sum(summands) - n
if r in summands:
    summands.remove(r)
print(len(summands))
print(*summands)
