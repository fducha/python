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

    def get_path(self, value):
        return self.path_to_root(self.find(value))

    def find(self, value):
        if self.value == value:
            return self
        else:
            if self.value is None:
                if self.has_children():
                    n = self.left.find(value)
                    if n is not None:
                        return n
                    else:
                        return self.right.find(value)
                else:
                    return None

    def path_to_root(self, node):
        path = ''
        p = node.parent
        while p is not None:
            if node is p.left:
                path = '0' + path
            if node is p.right:
                path = '1' + path
            node = p
            p = p.parent
        return path

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
chars = sorted(set(input_str))
for s in set(input_str):
    frequencies.append(Node(value=s, frequency=input_str.count(s)))
if len(frequencies) < 2:
    print(1, len(input_str))
    print('{}: 0'.format(frequencies[0].value))
    print('0' * len(input_str))
else:
    # frequencies.sort(key=lambda c: c.frequency)
    # for n in reversed(frequencies):
    #     chars.append(n.value)
    while len(frequencies) > 1:
        frequencies.sort(key=lambda c: c.frequency)
        p = Node()
        zero = frequencies[0]
        first = frequencies[1]
        if zero.value is None and first.value is not None:
            zero, first = first, zero
        p.set_children(zero, first)
        frequencies = [p] + frequencies[2:]

node = frequencies[0]
for s in chars:
    print(s, ':', node.get_path(s))
# print(node)
