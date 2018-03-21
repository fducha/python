class BinaryMaxHeap:
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

        triada = []
        if index <= size:
            triada.append(self.heap[index - 1])
        else:
            return
        i_child1 = index * 2
        if i_child1 <= size:
            triada.append(self.heap[i_child1 - 1])
        i_child2 = index * 2 + 1
        if i_child2 <= size:
            triada.append(self.heap[i_child2 - 1])
        i_max = self.heap.index(max(triada))
        if i_max != 0:
            self.heap[index - 1], self.heap[i_max] = self.heap[i_max], self.heap[index - 1]


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
