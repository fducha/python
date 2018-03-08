def fib(num):
    # if num == 1:
    #     return 0
    # if num == 2:
    #     return 1
    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b


# class FMatrix:
#     Q = [[1, 1], [1, 0]]
#
#     def __init__(self):
#         self.__memo = {}
#
#     def mul(self, M1, M2):
#         a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
#         a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
#         a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
#         a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
#         r = [[a11, a12], [a21, a22]]
#         return r
#
#     def pow(self, M, p):
#         if p == 1:
#             return M
#         if p in self.__memo:
#             return self.__memo[p]
#         K = self.pow(M, int(p / 2))
#         R = self.mul(K, K)
#         self.__memo[p] = R
#         return R
#
#     def get_fi(self, n):
#         if n == 0:
#             return 0
#         if n == 2:
#             return 1
#         if n == 1:
#             return 0
#         powers = [int(pow(2, b))
#                   for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']
#
#         matrices = [self.pow(FMatrix.Q, p)
#                     for p in powers]
#         while len(matrices) > 1:
#             M1 = matrices.pop()
#             M2 = matrices.pop()
#             R = self.mul(M1, M2)
#             matrices.append(R)
#         return matrices[0][0][0]


def fib_mod(n, m):
    # f = FMatrix()
    # return f.get_fi(n) % m
    if n == 1:
        return 1
    if n == 2:
        return 1
    k = 0
    s = [0, 1]
    for i in range(2, n):
        s.append((s[-1] + s[-2]) % m)
        # print(i, 's = {}'.format(s))
        k += 1
        if s[-1] == 1 and s[-2] == 0:
            print('n = {}, k = {}, s = {}'.format(n, k, s))
            break
    if k == 0:
        return n % m
    else:
        return s[n % k]


# n, m = map(int, input().split())
# n, m = 10, 2
# print(fib_mod(n, m))
# ff = FMatrix()
# print(ff.get_fi(3))

for i in range(1, 11):
    print(fib(i))
for n in range(1, 50):
    for m in range(2, 50):
        f = fib(n) % m
        fm = fib_mod(n, m)
        if f != fm:
            print('Failed test, n = {}, m = {}, fib(n) % m = {}, fib_mod = {}'.format(n, m, f, fm))
