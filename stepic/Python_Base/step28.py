import re, sys
print(*[re.sub(r'human', 'computer', line) for line in sys.stdin], sep='')