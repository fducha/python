class Thing:
    def __init__(self, cost, quantity):
        self.cost = cost
        self.quantity = quantity
        self.unit_price = cost / quantity

    def __repr__(self):
        return '<Thing: cost={}, quantity={}, unit price={}>'.format(self.cost, self.quantity, self.unit_price)


num_of_things, backpack_volume = map(int, input().split())
backpack = []
for i in range(num_of_things):
    c, q = map(int, input().split())
    backpack.append(Thing(c, q))
backpack.sort(key=lambda th: th.unit_price)
# print(backpack)
total_amount = 0.0
while backpack_volume > 0:
    if len(backpack) == 0:
        break
    thing = backpack.pop()
    if thing.quantity <= backpack_volume:
        total_amount += thing.cost
        backpack_volume -= thing.quantity
        continue
    else:
        total_amount += backpack_volume * thing.unit_price
        backpack_volume = 0
print('{0:.3f}'.format(total_amount))



