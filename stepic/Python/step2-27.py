import requests


def first_word_is_we(s: str) -> bool:
    return 'We' == s.split()[0]


url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'

text = requests.get(url).text.strip()

count = 1

while not first_word_is_we(text):
    url = 'https://stepik.org/media/attachments/course67/3.6.3/' + text.strip()
    print(count, end=' ')
    count += 1
    print('go to url: ' + url)
    text = requests.get(url).text.strip()

print(text)