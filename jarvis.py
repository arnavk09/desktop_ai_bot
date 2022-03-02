import pyttsx3
import speech_recognition as sr
import datetime as dt


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("It's quite late in the day. What would you like?")
    elif hour >= 6 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening ")


def takeCommand():
    '''Takes a command from user microphone and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        speak("Try saying it again!")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
