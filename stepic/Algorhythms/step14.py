class Segment:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __contains__(self, dot):
        return self.left <= dot <= self.right

    def __repr__(self):
        return '<Seg {} - {}>'.format(self.left, self.right)

    def __le__(self, other):
        return self.left <= other.left


def partition(lst, l, r):
    x = lst[l]
    j = l
    for i in range(l + 1, r):
        if lst[i] <= x:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def quick_sort(lst, l, r):
    if l >= r:
        return lst
    m = partition(lst, l, r)
    quick_sort(lst, l, m - 1)
    quick_sort(lst, m + 1, r)


def count_segs_for_dot(dot, segments):
    return len([s for s in segments if s.left <= dot <= s.right])


def quick_sort_approach(dots, segments):
    quick_sort(segments, 0, len(segments))
    print(*segments, sep='\n')


def main():
    seg_count, dot_count = map(int, input().split())
    segments = []
    for _ in range(seg_count):
        l, r = map(int, input().split())
        segments.append(Segment(l, r))
    for dot in input().split():
        print(count_segs_for_dot(int(dot), segments), end=' ')


if __name__ == '__main__':
    main()
