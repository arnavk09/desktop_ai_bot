import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("HAZEL VOICE IN REGISTRY : ", voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 6:
        speak("It's quite late in the night.")
    elif hour >= 6 and hour < 12:
        speak("good morning.")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon.")
    else:
        speak("good evening.")


speak("I am Hazel.")

if __name__ == "__main__":
    # speak("Hello World. I will be sentinent soon...")
    wishMe()
