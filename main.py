import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests
import json


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
    print(data)
    response(data)
    return data


def response(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save('speech/response.mp3')
    os.system('start speech/response.mp3')


listen()
