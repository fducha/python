import re, sys

print(*[line for line in sys.stdin if re.findall(r'\\', line)], sep='')