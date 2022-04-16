import speech_recognition as sr
from time import ctime
import time
from gtts import gTTS
from playsound import playsound


time.sleep(.5)


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
    playsound('speech/response.mp3')


def digital_assistant(data):
    if 'what is your name' in data:
        listening = True
        response('Doing Good')
    if 'what time is it' in data:
        listening = True
        response(ctime())
    if 'stop listening' in data:
        listening = False
        response('Have a great day')
        return listening
    return listening
