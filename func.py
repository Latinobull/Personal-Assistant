import os
import requests
from dotenv import load_dotenv
load_dotenv()


def dictonaryDefiniton(data):
    app_id = os.getenv('dictID')
    app_key = os.getenv('dictKey')
    language_code = 'en-us'
    word_id = ''
    data = data.split(' ')
    for i in range(0, len(data)):
        if data[i] == 'of':
            word_id = data[i+1]
    print(data)

    url = f'https://od-api.oxforddictionaries.com/api/v2/words/{language_code}?q={word_id}&fields=definitions'
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    definiton = r.json()
    definiton = definiton['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]
    print(definiton.get('definitions'))
    res = definiton.get('definitions')[0]
    return res
