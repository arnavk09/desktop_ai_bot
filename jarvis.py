import pyttsx3
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import datetime as dt
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

'''define all generic text blobs here '''

bye = "Bye, see you again."
acv = "According to Wikipedia, "


def timeNow():
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    print(type(ct))
    print("Current Time =", ct)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''announcer!'''
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 6:

        speak("It's quite late in the day. What do you want me to do? ")
    elif hour >= 6 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon! What do you want me to do? ")
    elif hour >= 18 and hour < 24:
        speak("Good evening! What do you want me to do?")


def takeCommand():
    '''Takes a command from user microphone and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Try saying it again!")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # WEB FUNCTIONALITY :

        if 'wikipedia' in query:
            speak("Searching Wikipedia for your query..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(acv)
            print(acv, results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open_new_tab("youtube.com")
        elif 'play music' in query:
            music_dir = "E:\\Downloads\\Music\\Eminem"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
