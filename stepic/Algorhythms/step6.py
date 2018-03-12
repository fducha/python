class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.marked = False

    def __contains__(self, item):
        return self.start <= item <= self.end

    def __repr__(self):
        return 'Segment: {} - {}'.format(self.start, self.end)


def is_point_right(point: int, segments: list) -> bool:
    for s in filter(lambda s: s.marked, segments):
        if point == s.end:
            return True
    return False


def my_sort(lst: list):
    for i in range(len(lst)):
        for j in range(len(lst)):
            pass


segments = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    segments.append(Segment(a, b))

min_points = set()
for seg in sorted(segments, key=lambda seg: seg.end):
    if is_point_right(seg.end, segments):
        continue
    min_points.add(seg.end)
    seg.marked = True
    for s in filter(lambda s: not s.marked, segments):
        if seg.end in s:
            s.marked = True

print(len(min_points))
print(*min_points)


for p in min_points:
    cont = False
    for seg in segments:
        if p in seg:
            cont = True
            break
    print(p, 'OK' if cont else 'FAIL !!!')
