import speech_recognition as sr

def listen() -> str:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1  
        r.energy_threshold = 300 
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand, please try again.")
        return ""
    except sr.RequestError:
        print("Speech service unavailable.")
        return ""