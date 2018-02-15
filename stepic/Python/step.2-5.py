# a, b = [int(input()) for i in range(2)]
# count, s = 0, 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         s += i
#         count +=1
# print(s / count)


a,b = int(input()), int(input())
a += -a%3
b -= b%3
print((a+b)/2)