import speech_recognition as sr
import datetime
import subprocess
import pyttsx3
import webbrowser
import pywhatkit

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate_speech=engine.getProperty('rate')
engine.setProperty('rate',rate_speech-100)
engine.say("Hello ujwal how is your day going")
engine.runAndWait()
recognizer=sr.Recognizer()


def command():
        with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration=0.5)
                print("Tell U R command Sir")
                record=recognizer.listen(source)
        try:
               text=recognizer.recognize_google(record,language='en_US')
               text=text.lower()
               print(f"Your Command {text}")
        except Exception as ex:
               print(ex)
    
        if 'chrome'in text:
            engine.say('Opening Chrome')
            engine.runAndWait()
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([chrome_path])
            
               

                
                 


while True:
    command()   
