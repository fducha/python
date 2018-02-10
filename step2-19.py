words = input().split()

result = {}

for w in words:
    result.setdefault(w.lower(), 0)
    result[w.lower()] += 1

for k, v in result.items():
    print(k, v)
