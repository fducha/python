class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, obj):
        if obj > 0:
            super().append(obj)
        else:
            raise NonPositiveError()


lst = PositiveList()
lst.append(1)
print(*lst)
lst.append(0)
print(*lst)
lst.append(-1)
print(*lst)