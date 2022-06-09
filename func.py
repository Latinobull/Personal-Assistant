import os
import requests
from dotenv import load_dotenv
import webbrowser
from db.routes import Database
load_dotenv()

DB = Database()


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


def getWeather(data):
    APIKEY = os.getenv('API-KEY')
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    data = data.split(" ")
    location = str(data[5])
    url = f'{weather_url}appid={APIKEY}&q={location} '
    js = requests.get(url).json()
    if js["cod"] != "404":
        weather = js["main"]
        temp = round((weather["temp"] - 273.15) * 9/5 + 32)
        hum = weather["humidity"]
        desc = js["weather"][0]["description"]
        resp_string = f'The temperature is{str(temp)} The humidity is {str(hum)} and The weather description is {str(desc)}'

        return resp_string
    else:
        return"City Not Found"


def googleSearch(data):
    data = data.split(' ')
    data = ' '.join(data[2:])
    location_url = f'https://www.google.com/search?q={data}'
    webbrowser.get().open_new_tab(location_url)
    return f'Here is {data} on Google'


def locationSearch(data):
    data = data.split(" ")
    data = ' '.join(data[2:])
    location_url = f'https://www.google.com/maps/place/{str(data)}'
    webbrowser.get().open_new_tab(location_url)
    return f'Here is {data}.'


def findUser():
    user = DB.findUser()
    return user

def createUser(data):
    DB.createUser(data)

