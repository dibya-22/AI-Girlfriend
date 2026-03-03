import os
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import play

load_dotenv()
client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

def speak(speech: str, voice: str = "shreya"):
    try:
        audio = client.text_to_speech.convert(
            target_language_code="en-IN",
            text=speech,
            model="bulbul:v3",
            speaker=voice
        )
        play(audio)
    except Exception as e:
        print(f"TTS failed: {e}")
        print(f"🤖: {speech}")