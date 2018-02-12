import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/699.txt'

r = requests.get(url)

print(r.text.splitlines())

