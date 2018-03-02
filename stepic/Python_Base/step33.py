import re, requests

urlA, urlB = input().strip(), input().strip()
dataA = requests.get(urlA)
result = 'No'
if dataA.status_code != '404':
    urls = re.findall(r'a href="(.+)"', dataA.text)
    for url in urls:
        data = requests.get(url)
        if data.status_code != '404':
            urls2 = re.findall(r'a href="(.+)"', data.text)
            if urlB in urls2:
                result = 'Yes'
                break
print(result)

