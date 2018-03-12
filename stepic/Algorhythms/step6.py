from random import randint

class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.marked = False

    def __contains__(self, item):
        return self.start <= item <= self.end

    def __repr__(self):
        return 'Segment: {} - {}'.format(self.start, self.end)


# def my_sort(lst: list):
#     for i in range(len(lst) - 1):
#         for j in range(i + 1, len(lst)):
#             if lst[i].end > lst[j].end:
#                 lst[i], lst[j] = lst[j], lst[i]
#             elif lst[i].end == lst[j].end:
#                 if lst[i].start > lst[j].start:
#                     lst[i], lst[j] = lst[j], lst[i]


segments = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    # a = randint(0, 100)
    # b = randint(a, 100)
    if a > b:
        a, b = b, a
    segments.append(Segment(a, b))

min_points = set()
print(segments)
segments.sort(key=lambda s: s.end)
print('Sorted', segments)

for seg in segments:
    if seg.marked:
        continue
    min_points.add(seg.end)
    seg.marked = True
    for s in filter(lambda s: not s.marked, segments):
        if seg.end in s:
            s.marked = True

print(len(min_points))
print(*min_points)


for s in segments:
    has_dot = False
    for dot in min_points:
        if dot in s:
            has_dot = True
            break
    print(s, 'test', 'OK, dot {}'.format(dot) if has_dot else 'FAIL!!!!!!!')
