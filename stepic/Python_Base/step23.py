import re
import sys

result = []
for line in sys.stdin:
    # if not line:
    #     break
    line = line.strip()
    if re.match(r'(.*(cat).*){2}', line):
        result.append(line)

print(*result, sep='\n')
