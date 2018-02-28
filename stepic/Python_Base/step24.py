import re, sys

print(*[line for line in sys.stdin if re.findall(r'\bcat\b', line)], sep='')
