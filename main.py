import func
import os
import speech_recognition as sr
import datetime
import time
from gtts import gTTS
from playsound import playsound


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

        response(func.locationSearch(data))
    if 'show me' in data:
        listening = True
        response(func.googleSearch(data))
    if 'what is the weather in' in data:
        listening = True
        response(func.getWeather(data))
    if 'definition' in data:
        listening = True
        response(func.dictonaryDefiniton(data))
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
