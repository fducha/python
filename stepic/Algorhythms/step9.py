input_str = input()
frequency = {}
for s in set(input_str):
    frequency.setdefault(s, 0)
    frequency[s] = input_str.count(s)
# frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))
print(frequency)