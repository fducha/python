s, a, b = input(), input(), input()

if a in s and a in b:
    print('Impossible')
else:
    replace_count = 0
    repl_s = s.replace(a, b)
    while s != repl_s:
        replace_count += 1
        s = repl_s[:]
        repl_s = s.replace(a, b)
    print(replace_count)
