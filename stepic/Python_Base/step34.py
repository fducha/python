import re, requests

text = requests.get(input().strip()).text
hrefs = re.findall(r'href=".+?"', text, re.IGNORECASE)
hrefs.extend(re.findall(r'href=\'.+?\'', text, re.IGNORECASE))
urls = set()
for href in hrefs:
    t = href.split('//')
    t = t[1] if len(t) > 2 else t[-1]
    if '.png' in t: continue
    if '.css' in t: continue
    t = t.split('/')[0].split('?')[0].split(':')[0]
    t = t.replace('"', '')
    t = t.replace('href=', '')
    t = t.replace('\'', '')
    if t == '..': continue
    urls.add(t)
urls = sorted(list(urls))
print(*urls, sep='\n')

tests = []
with open('test_step34_3.txt') as f:
    for row in f:
        tests.append(row.strip())

# with open('test_step34_2.txt') as f:
#     for row in f:
#         tests.append(row.strip())

for u in urls:
    if u in tests:
        print(u, 'is OK')
    else:
        print(u, 'is FAILED !!!!!!!!!!!!!!!!!!!')