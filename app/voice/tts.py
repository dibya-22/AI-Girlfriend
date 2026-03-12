import os
from utils.color_print import forecolor
from routes.auth import get_accent
from dotenv import load_dotenv

load_dotenv()

def sarvam(speech: str, voice: str = "shreya"):
    """
    * TTS using Sarvam AI — best for Indian accent
    ? voice options: shreya, arvind, amol, amartya, diya, neel, maitreyi, pavithra, barani, calya, saurabh
    ! requires SARVAM_API_KEY in .env
    """
    from sarvamai import SarvamAI
    from sarvamai.play import play
    sclient = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    audio = sclient.text_to_speech.convert(
        target_language_code="en-IN",
        text=speech,
        model="bulbul:v3",
        speaker=voice
    )
    play(audio)

def elab(speech: str, voice: str = "Rachel"):
    """
    * TTS using ElevenLabs — best for American accent
    ? voice options: Rachel, Domi, Bella, Antoni, Elli, Josh, Arnold, Adam, Sam
    ! requires ELEVENLABS_API_KEY in .env
    """
    from elevenlabs.client import ElevenLabs
    from elevenlabs.play import play
    eclient = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    #? Elevenlab Voice Ids
    VOICES = {
        "Rachel": "21m00Tcm4TlvDq8ikWAM",
        "Domi": "AZnzlk1XvdvUeBnXmlld",
        "Bella": "EXAVITQu4vr4xnSDxMaL",
        "Antoni": "ErXwobaYiN019PkySvjV",
        "Elli": "MF3mGyEYCl7XYWbV9V6O",
        "Josh": "TxGEqnHWrfWFTfGW9XjX",
        "Arnold": "VR6AewLTigWG4xSOukaG",
        "Adam": "pNInz6obpgDQGcFmaJgB",
        "Sam": "yoZ06aMxZJJ28mfd3POQ",
    }

    audio = eclient.text_to_speech.convert(
        text=speech,
        voice_id=VOICES.get(voice),
        model_id="eleven_turbo_v2_5",
        output_format="mp3_44100_128",
    )

    play(audio)


def speak(speech: str, user_id: str, voice: str = None):
    """
    * Routes TTS to Sarvam or ElevenLabs based on user's accent preference
    ? indian accent → sarvam, american accent → elevenlabs
    ! falls back to text print if TTS fails
    """
    try:
        accent = get_accent(user_id)


        if accent == "american":
            elab(speech, voice or "Rachel")
        else:
            sarvam(speech, voice or "shreya")
    except Exception as e:
        print(forecolor(f"TTS failed: {e}", "red")) 
        print(f"🤖: {forecolor(speech, 'white')}\n") #! fallback to text if voice fails