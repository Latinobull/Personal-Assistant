from operator import truediv
import os
import speech_recognition as sr
import datetime
import time
from gtts import gTTS
from playsound import playsound
import webbrowser
from dotenv import load_dotenv
import requests
load_dotenv()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am Listening')
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        print(f'You said {data}')
    except sr.UnknownValueError:
        print('Google could not recognize what you said')
    except sr.RequestError as err:
        print(f'Requested failed; {err}')
    return data


def response(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save(f'speech/response.mp3')
    playsound(f'speech/response.mp3')
    os.remove('speech/response.mp3')


def digital_assistant(data):
    if 'what is your name' in data:
        print(data)
        listening = True
        response('My name is Ria and I am your personal assistant')
    if 'what time is it' in data:
        listening = True
        x = str(datetime.datetime.now().strftime('%H:%M %p'))
        response(x)
    if "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = f'https://www.google.com/maps/place/{str(data[2])}'
        response("Hold on DJ, I will show you where " + data[2] + " is.")
        webbrowser.get().open_new_tab(location_url)
        listening = False
        response('Have a great day')
    if 'show me' in data:
        listening = True
        data = data.split(' ')
        data = ' '.join(data[2:])
        location_url = f'https://www.google.com/search?q={data}'
        response(f'Here is {data} on Google')
        webbrowser.get().open_new_tab(location_url)
        print(data)
    if 'what is the weather in' in data:
        listening = True
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
            resp_string = " The temperature is " + \
                str(temp) + " The humidity is " + str(hum) + \
                " and The weather description is " + str(desc)
            response(resp_string)
        else:
            response("City Not Found")

    if data == '':
        listening = False
        response('Have a great day')
        return listening
    return listening


time.sleep(.5)
response('How can I help You DJ?')
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)
