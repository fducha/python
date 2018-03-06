import requests
import json


app_name = 'python_stepic'
client_id = 'fe516fbc6479702002a8'
client_secret = '186bb1328c7e6720d5c0f2dd6610f761'

r = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                  data={
                        'client_id': client_id,
                        'client_secret': client_secret
                    })
json_response = json.loads(r.text)
token = json_response['token']

results = {}
headers = {'X-Xapp-Token': token}
with open('dataset_24476_4.txt') as ifile:
    for row in ifile:
        row = row.strip()
        url = 'https://api.artsy.net/api/artists/{}'.format(row)
        data = json.loads(requests.get(url, headers=headers).text)
        birthday = int(data['birthday'])
        name = data['sortable_name']
        results.setdefault(birthday, [])
        results[birthday].append(name)
        print(birthday, name)

with open('out_step38.txt', 'w') as ofile:
    for year, names in sorted(results.items()):
        print(*sorted(names), sep='\n', file=ofile)

