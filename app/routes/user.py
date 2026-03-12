import os
from utils.pass_input import pass_input
from utils.color_print import backcolor
from routes.auth import run_auth
import questionary

def Auth():        
    action = questionary.select(
        "What do you want to do?",
        choices=["Login", "Signup"],
    ).ask().lower()

    os.system("cls")
    print(f"{backcolor('__LOGIN__', "cyan", "bright") if action == 'login' else backcolor('__SIGN UP__', "cyan", "bright")}")

    username = input("Username: ")
    password = pass_input()

    persona = None
    mode = None


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
            
    
        result = run_auth(action, username, password, persona, mode, accent)
    else:
        result = run_auth(action, username, password)

    if result is None:
        return None
    else:
        return {
            "username": result["username"],
            "user_id": result["user_id"],
            "persona": result["persona"],
            "mode": result["mode"],
        }

