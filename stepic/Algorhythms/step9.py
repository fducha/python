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


class Haffmann:
    def __init__(self, source):
        self.source = source
        self.nodes = self._get_freqs()
        if len(self.nodes) == 1:
            self.root = self.nodes[0]
            self.code = '0' * len(self.source)
            self.alphabet = {self.root.value: '0'}
        else:
            self.alphabet = {}
            self.root = self._get_root()
            self.code = self._get_code()

    def _sort_by_frequency(self, nds: list):
        size = len(nds)
        if size > 1:
            for i in range(size - 1):
                for j in range(i + 1, size):
                    if nds[i].frequency > nds[j].frequency:
                        nds[i], nds[j] = nds[j], nds[i]
                    elif nds[i].frequency == nds[j].frequency:
                        if nds[i].value is None or nds[j].value is None:
                            continue
                        if nds[i].value > nds[j].value:
                            nds[i], nds[j] = nds[j], nds[i]

    def _get_freqs(self):
        res = []
        for s in set(self.source):
            res.append(Node(value=s, frequency=self.source.count(s)))
        self._sort_by_frequency(res)
        self.sorted_letters = sorted([x.value for x in res])
        return res

    def _get_root(self):
        while len(self.nodes) > 1:
            self._sort_by_frequency(self.nodes)
            p = Node()
            zero, first = self.nodes[0], self.nodes[1]
            if zero.value is None and first.value is not None:
                zero, first = first, zero
            p.set_children(zero, first)
            self.nodes = [p] + self.nodes[2:]
        for l in self.sorted_letters:
            self.alphabet[l] = self.nodes[0].get_path(l)
        return self.nodes[0]

    def letter_code(self, letter):
        if letter in self.source:
            return self.alphabet[letter]

    def _get_code(self):
        res = []
        for l in self.source:
            res.append(self.alphabet[l])

        return ''.join(res)


hc = Haffmann(input())
print(len(hc.sorted_letters), len(hc.code))
for l in hc.sorted_letters:
    print('{}: {}'.format(l, hc.letter_code(l)))
print(hc.code)
