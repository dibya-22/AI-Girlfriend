import os
from utils.pass_input import pass_input
from utils.color_print import forecolor, backcolor
from routes.auth import run_auth
import questionary

def Auth():        
    action = questionary.select(
        "What do you want to do?",
        choices=["Login", "Signup"],
    ).ask().lower()

    os.system("cls")
    print(f"{backcolor('__LOGIN__', 'cyan', 'bright') if action == 'login' else backcolor('__SIGN UP__', 'cyan', 'bright')}")

    persona = None
    mode = None
    accent = None


    if action == "signup":
        #* Persona Select
        persona = questionary.select(
            "Choose AI's Persona:",
            choices=["Girlfriend", "Boyfriend", "Friend"],
        ).ask().lower()
    
        #* Mode Select
        mode = questionary.select(
            "Choose your prefered mode to talk.",
            choices=["Text", "Voice"],
        ).ask().lower()

        accent = questionary.select(
            "Select Your Accent: ",
            choices=["Indian", "American"],
        ).ask().lower()
            
        result = None
        for attempt in range(3):
            username = input("Username: ")
            password = pass_input()
    
            result = run_auth(action, username, password, persona, mode, accent)
            if result is not None:
                break
            if attempt < 2:
                print(forecolor(f"Try another username. {2 - attempt} attempt(s) left.", "yellow"))
    else:
        username = input("Username: ")
        result = None
        for attempt in range(3):
            password = pass_input()
            result = run_auth(action, username, password)
            if result is not None:
                break
            if attempt < 2:
                print(forecolor(f"Try again. {2 - attempt} attempt(s) left.", "yellow"))

    if result is None:
        return None
    else:
        return {
            "username": result["username"],
            "user_id": result["user_id"],
            "persona": result["persona"],
            "mode": result["mode"],
        }

