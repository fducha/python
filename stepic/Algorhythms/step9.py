class LetterString:
    def __init__(self, string):
        self.string = string[:]
        self.char_frequency = {}
        for s in set(self.string):
            self.char_frequency.setdefault(s, 0)
            self.char_frequency[s] = self.string.count(s)
        self.char_frequency = sorted(self.char_frequency.items(), key=lambda x: x[1])
        self.char_code = {}

    def count(self):
        return len(set(self.string))


class HaffmanCode:
    def __init__(self, ls: LetterString):
        self.lstring = ls
        self.encode()

    def encode(self):
        pass

    def __repr__(self):
        return self.lstring.string


code = HaffmanCode(LetterString(input()))
print(code)