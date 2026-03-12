import speech_recognition as sr
from utils.color_print import forecolor

def listen() -> str:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1  
        r.energy_threshold = 300 
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print(forecolor("Could not understand, please try again.", "red"))
        return ""
    except sr.RequestError:
        print(forecolor("Speech service unavailable.", "red"))
        return ""