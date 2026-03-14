import os
from utils.color_print import forecolor
from routes.auth import get_speak_details
from dotenv import load_dotenv
from sarvamai import SarvamAI
from elevenlabs.client import ElevenLabs
from sarvamai.play import play as sarvam_play
from elevenlabs.play import play as elab_play

load_dotenv()

def sarvam(speech: str, persona: str):
    """
    * TTS using Sarvam AI — best for Indian accent
    ? voice options: shreya, arvind, amol, amartya, diya, neel, maitreyi, pavithra, barani, calya, saurabh
    ! requires SARVAM_API_KEY in .env
    """

    VOICES = {
        "girlfriend": "ishita",
        "boyfriend": "ratan",
        "friend": "mani"
    }
    
    sclient = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    audio = sclient.text_to_speech.convert(
        target_language_code="en-IN",
        text=speech,
        model="bulbul:v3",
        speaker=VOICES.get(persona)
    )
    sarvam_play(audio)

def elab(speech: str, persona: str):
    """
    * TTS using ElevenLabs — best for American accent
    ? voice options: Serafina, Adam, Amy
    ! requires ELEVENLABS_API_KEY in .env
    """
    
    eclient = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    #? Elevenlab Voice Ids
    VOICES = {
        "girlfriend": "hpp4J3VqNfWAUOO0d1Us", # Bella
        "boyfriend": "bIHbv24MWmeRgasZH58o", # Will
        "friend": "hpp4J3VqNfWAUOO0d1Us" # Janet
    }

    audio = eclient.text_to_speech.convert(
        text=speech,
        voice_id=VOICES.get(persona),
        model_id="eleven_turbo_v2_5",
        output_format="mp3_44100_128",
    )

    elab_play(audio)


def speak(speech: str, user_id: str, voice: str = None):
    """
    * Routes TTS to Sarvam or ElevenLabs based on user's accent preference
    ? indian accent → sarvam, american accent → elevenlabs
    """
    try:
        accent, persona = get_speak_details(user_id)


        if accent == "american":
            elab(speech, persona)
        else:
            sarvam(speech, persona)
    except Exception as e:
        print(forecolor(f"TTS failed: {e}", "red")) 