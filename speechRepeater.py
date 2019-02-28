import speech_recognition as sr
import pyttsx3
import threading
import sys

'Create a Custom Thread Class'
class myFred(threading.Thread):
    'Initialise Thread'
    def __init__(self):
        threading.Thread.__init__(self)

    'Run the Speech Listener in a endless loop'
    def run(self):
        'The Say statement for the machine'
        engine.say('Speak anything')
        'Run Statement'
        engine.runAndWait()
        while True:
            with sr.Microphone() as source:
                try:
                    'Listened of every word you said'
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    engine.say(text)
                    engine.runAndWait()
                    word = 'bye'
                    'Will Check if Word is bye--> not ready yet'
                    '''
                    if word in text.lower:
                        sys.exit(0)
                    '''
                    
                except:
                    'If it could not understand the word said'
                    engine.say('I haven\'t understand anything.')
                    engine.runAndWait()
                    
'Initialise the speaker'
engine = pyttsx3.init()
'set a slower speech rate to understand the machine word said'
engine.setProperty('rate',100)
'set a default installed language on windows'
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
'Initalise the Speechlistener'
r = sr.Recognizer()

'Initialise the Thread'
t1 = myFred()

'Start the Thread'
t1.start()



