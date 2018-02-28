import re, sys
print(*[re.sub(r'(\w)\1+', r'\1', line) for line in sys.stdin], sep='')