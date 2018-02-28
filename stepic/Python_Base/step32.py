import re, sys

print(*[line.strip() for line in sys.stdin if re.fullmatch(r'((0|11)|(10(1|00)*01))*', line.strip())], sep='\n')