import speech_recognition as sr
import datetime
import subprocess
import pyttsx3
import webbrowser
import pywhatkit
from GoogleNews import GoogleNews
import time



engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate_speech=engine.getProperty('rate')
engine.setProperty('rate',rate_speech-100)
recognizer=sr.Recognizer()
googlenews=GoogleNews(lang='en')


def command():
        with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration=1)
                print("Tell U R command Sir")
                record=recognizer.listen(source)
        try:
               text=''
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
        if 'class' in text:
            engine.say('attding class')
            engine.runAndWait()
            webbrowser.open('http://meet.google.com/fpk-qmpw-wmh')
        if 'play' in text:
              engine.say("Playing your songs ")
              engine.runAndWait()
              webbrowser.open('https://www.youtube.com/watch?v=99138T2WeOQ&list=RDEM0OjgBssMTWIQmajDQFuXGA&start_radio=1')
        if 'headlines' in text:
              engine.say("Getting news for u")
              engine.runAndWait()
              googlenews.get_news('Today news')
              googlenews.result(sort=True)
              news=googlenews.get_texts()
              print(*news[1:5],sep=',')
            #   engine.say(news)
            #   engine.runAndWait()
        if 'blockchain' in text:
              engine.say("Today crypto news ")
              engine.runAndWait()
              googlenews.get_news('blockchain and Crypto news')
              googlenews.result(sort=True)
              news=googlenews.get_texts()
              print(*news[1:5],sep=',')
            #   engine.say(news)
            #   engine.runAndWait()


while True:
    command()  

    