import re, sys

print(*[line for line in sys.stdin if re.findall(r'z.{3}z', line)], sep='')