import speech_recognition as sr
import pyttsx3
import threading
import sys


class myFred(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        engine.say('Speak anything')
        engine.runAndWait()
        while True:
            with sr.Microphone() as source:
                try:
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    engine.say(text)
                    engine.runAndWait()
                    word = 'bye'
                    if word in text.lower:
                        sys.exit(0)
                    
                    
                except:
                    engine.say('I haven\'t understand anything.')
                    engine.runAndWait()
                    

engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
r = sr.Recognizer()



t1 = myFred()

t1.start()



