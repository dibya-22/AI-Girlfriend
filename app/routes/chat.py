from chains.chat import chat, get_graph
from routes.auth import update_mode
from memory.user_memory import add_memory
from voice.stt import listen
from voice.tts import speak
from utils.color_print import forecolor

def start_chat(user: dict):
    user_id = user["user_id"]
    mode = user.get("mode", "text")
    persona = user.get("persona") or "friend"

    
    with get_graph() as checkpointer:
        while True:
            if mode == "voice":
                print(forecolor(">", "yellow", "bright"), end="", flush=True)
                user_input = listen()
                print(forecolor(">", "yellow", "bright"), end="", flush=True)
                print(user_input) 
            else:
                user_input = input(forecolor(">> ", "blue", "bright"))

            if not user_input:
                if mode == "voice":
                    speak("Invalid Input! Please Enter Again", user_id)
                print(forecolor("Invalid Input! Please Enter Again", "red", "bright"))
                continue

            response, new_mode, should_terminate = chat(user_input, user_id, persona, checkpointer)

            if mode == "voice":
                speak(response, user_id)
                print(f"🤖: {forecolor(response, 'white')}\n")
            else:
                print(f"🤖: {forecolor(response, 'white')}\n")

            add_memory(user_input, response, user_id)

            if should_terminate:
                if mode == "voice":
                    speak("Bye! Talk soon", user_id)
                print(f"🤖: {forecolor('Bye! Talk soon 💕', 'white')}\n")
                break

            if new_mode and new_mode != mode:
                mode = new_mode
                update_mode(user_id, mode) #* save to DB
                if mode == "voice":
                    speak(f"Switched to {mode} mode", user_id)
                print(f"[Switched to {forecolor(mode, 'cyan', 'dim')} mode]")
