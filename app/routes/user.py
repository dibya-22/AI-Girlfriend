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
            if result == "user_already_exist":
                print(forecolor("Username already taken.", "red"))
                if attempt < 2:
                    print(forecolor(f"Try another. {2 - attempt} attempt(s) left.", "yellow"))
            else:
                break
    else:
        username = input("Username: ")
        result = None
        for attempt in range(3):
            password = pass_input()
            result = run_auth(action, username, password)
            if result == "user_not_found":
                print(forecolor("Username not found. Please Sign up", "red"))
                result = None
                break
            elif result == "wrong_password":
                print(forecolor("Wrong password.", "red"))
                if attempt < 2:
                    print(forecolor(f"Try again. {2 - attempt} attempt(s) left.", "yellow"))
            else:
                break

    if result is None or isinstance(result, str):
        return None
    else:
        return {
            "username": result["username"],
            "user_id": result["user_id"],
            "persona": result["persona"],
            "mode": result["mode"],
        }

