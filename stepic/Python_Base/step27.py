import re, sys
print(*[line for line in sys.stdin if re.findall(r'\b(.+)(\1)\b', line)], sep='')