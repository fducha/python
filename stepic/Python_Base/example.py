# lst = [1, 2, 3, 4, 5, 6]
# book = {
#     'title': 'Облачный атлас',
#     'author': 'Дэвид Митчелл',
#     'year_published': 1999
# }
#
# string = 'Hello fucking guys!!'
#
# it = iter(string)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break

from random import random


# class RandomIterator:
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration


# for x in RandomIterator(10):
#     print(x)


# def random_generator(k):
#     for i in range(k):
#         yield random()
#
#
# gen = random_generator(3)
# for i in gen:
#     print(i)


a = (i + 1 for i in range(4))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

