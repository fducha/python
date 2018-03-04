import requests, json

with open('dataset_24476_3.txt') as file, open('res.txt', 'w') as out:
    for num in file:
        num = int(num.strip())
        url_template = 'http://numbersapi.com/{}/math?json=true'.format(num)
        print('Interesting' if json.loads(requests.get(url_template).text)['found'] else 'Boring', file=out)
