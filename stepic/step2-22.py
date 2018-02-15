with open('dataset_3363_3.txt') as f:
    res = {}
    for s in f:
        words = s.strip().split()
        for w in words:
            res.setdefault(w.lower(), 0)
            res[w.lower()] += 1
    print(res)
    max_keys = []
    m = max(res.values())
    print(m)
    for k, v in res.items():
        if v == m:
            max_keys.append(k)
    print(min(max_keys), m)
