import re, sys
print(*[re.sub(r'[Aa]+\b', 'argh', line, count=1) for line in sys.stdin], sep='')