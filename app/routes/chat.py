from chains.chat import chat, get_graph
from memory.user_memory import add_memory
from voice.stt import listen
from voice.tts import speak

def start_chat(user: dict):
    user_id = user["user_id"]
    mode = user.get("mode", "text")
    persona = user.get("persona", "friend")

    
    with get_graph() as checkpointer:
        while True:
            if mode == "voice":
                print(">", end=" ", flush=True)
                user_input = listen()
                print(user_input)
            else:
                user_input = input("> ")

            if not user_input:
                if mode == "voice":
                    speak("Invalid Input! Please Enter Again")
                print("Invalid Input! Please Enter Again")
                continue

            response, new_mode, should_terminate = chat(user_input, user_id, persona, checkpointer)

            if mode == "voice":
                speak(response)
                print(f"🤖: {response}\n")
            else:
                print(f"🤖: {response}\n")

            add_memory(user_input, response, user_id)

            if should_terminate:
                if mode == "voice":
                    speak("Bye! Talk soon")
                print("🤖: Bye! Talk soon 💕")
                break

            if new_mode and new_mode != mode:
                mode = new_mode
                print(f"[Switched to {mode} mode]")
