class Char:
    def __init__(self, chr, fr):
        self.chr = chr
        self.frequency = fr


class Node:
    def __init__(self, value=None, frequency=0, parent=None):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
        self.parent = parent

    def set_children(self, left, right):
        self.left = left
        left.parent = self
        self.right = right
        right.parent = self
        self.frequency = left.frequency + right.frequency

    def has_children(self):
        return self.left is not None and self.right is not None

    def __repr__(self):
        if not self.has_children():
            return '<Node {} ({})>'.format(self.value, self.frequency)
        return '<Node {} ({}): left {}, right {}>'.format(self.value, self.frequency, self.left, self.right)


input_str = input()
frequencies = []
for s in set(input_str):
    frequencies.append(Node(value=s, frequency=input_str.count(s)))
if len(frequencies) < 2:
    print(1, len(input_str))
    print('{}: 0'.format(frequencies[0].value))
    print('0' * len(input_str))
else:
    while len(frequencies) > 1:
        frequencies.sort(key=lambda c: c.frequency)
        p = Node()
        p.set_children(frequencies[0], frequencies[1])
        frequencies = [p] + frequencies[2:]
        print(frequencies)
