class BinaryMaxHeap:
    """Heap indexes are started from 1 for _siftUp and _siftDown methods"""

    def __init__(self):
        self.heap = []

    def insert(self, value: int) -> None:
        self.heap.append(value)
        i_current = len(self.heap)
        self._siftUp(i_current)

    def extract_max(self) -> int:
        if len(self.heap) == 1:
            return self.heap.pop()
        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftDown(1)
        return max

    def _siftUp(self, index: int) -> None:
        if index < 2:
            return
        parent_index = int(((index - 1) / 2) + 0.5)
        while self.heap[index - 1] > self.heap[parent_index - 1]:
            self.heap[index - 1], self.heap[parent_index - 1] = self.heap[parent_index - 1], self.heap[index - 1]
            index = parent_index
            parent_index = int(((index - 1) / 2) + 0.5)
            if parent_index == 0:
                break

    def _siftDown(self, index: int) -> None:
        size = len(self.heap)
        if size == 1:
            return

        max_child_value = 1000000001
        current_value = self.heap[index - 1]

        while current_value < max_child_value:
            # index left child
            ilc = index * 2
            # if ilc out of range heap
            if ilc > size:
                max_child_value = -1
                continue
            # index right child
            irc = ilc + 1
            # if irc in range heap
            if irc <= size:
                # get index of max child (that bigger other)
                imc = ilc if self.heap[ilc - 1] >= self.heap[irc - 1] else irc
            else:
                imc = ilc
            max_child_value = self.heap[imc - 1]
            if current_value < max_child_value:
                self.heap[index - 1], self.heap[imc - 1] = self.heap[imc - 1], self.heap[index - 1]
                index = imc
                current_value = self.heap[index - 1]
                max_child_value = 1000000001


commands = []
for _ in range(int(input())):
    commands.append(input())

bmh = BinaryMaxHeap()
for c in commands:
    if c.startswith('Insert'):
        _, num = c.split()
        bmh.insert(int(num))
    elif c == 'ExtractMax':
        print(bmh.extract_max())

# print(bmh.heap)
