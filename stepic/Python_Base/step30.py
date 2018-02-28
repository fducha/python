import re, sys
print(*[re.sub(r'(\b)(\w)(\w)(\w*)(\b)', r'\1\3\2\4\5', line) for line in sys.stdin], sep='')