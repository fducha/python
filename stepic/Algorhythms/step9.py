class Char:
    def __init__(self, chr, fr):
        self.chr = chr
        self.frequency = fr


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


input_str = input()
frequencies = []
for s in set(input_str):
    frequencies.append(Char(s, input_str.count(s)))
if len(frequencies) < 2:
    print(1, len(input_str))
    print('{}: 0'.format(frequencies[0].chr))
    print('0' * len(input_str))
else:
    frequencies.sort(key=lambda c: c.frequency)
    l = Node(frequencies[0].chr)
    r = Node(frequencies[1].chr)
    p = Node(frequencies[0].frequency + frequencies[1].frequency)
    l.parent = p
    r.parent = p
    frequencies = [p] + frequencies[2:]
    print(frequencies)
