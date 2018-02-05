genom = list(input())
cur = genom.pop()
count = 1
res = []
while genom:
  prev = genom.pop()
  if cur == prev:
    count += 1
    continue
  else:
    res.append(str(count))
    res.append(cur)
    cur = prev
    count = 1
res.append(str(count))
res.append(cur)
print(''.join(reversed(res)))
