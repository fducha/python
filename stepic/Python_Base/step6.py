class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity <= self.count + v

    def add(self, v):
        if self.can_add(v):
            self.count += v


mb = MoneyBox(10)
print(mb.count)
mb.add(5)
print(mb.count)
mb.add(4)
print(mb.count)
mb.add(3)
print(mb.count)