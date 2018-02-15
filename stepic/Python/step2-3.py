lst = []
while True:
    num = int(input())
    if num < 10:
        continue
    elif num > 100:
        break
    lst.append(num)
for i in lst:
    print(i)
