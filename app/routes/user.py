import os
from utils.pass_input import pass_input
from routes.auth import run_auth

def Auth():
    choice = input("1. Login\n2. Sign Up\nChoose: ").lower()
    match choice:
        case "1" | "login":
            action = "login"
        case "2" | "sign up" | "signup" | "sign-up":
            action = "signup"
        case _:
            print("Invalid choice")
            return None

    os.system("cls")
    print(f"{'__LOGIN__' if action == 'login' else '__SIGN UP__'}")
    username = input("Username: ")
    password = pass_input()

    persona = None
    mode = None

    if action == "signup":
        print("__PERSONA__")
        choice = input("1. Girlfriend\n2. Boyfriend\n3. Friend\nChoose: ").lower()
        match choice:
            case "1" | "girlfriend" | "girl-friend" | "gf":
                persona = "girlfriend"
            case "2" | "boyfriend" | "boy-friend" | "bf":
                persona = "boyfriend"
            case "3" | "friend":
                persona = "friend"
            case _:
                print("Invalid choice")
                return None
    
        print("__MODE__")
        choice = input("1. Text\n2. Voice\nChoose: ").lower()
        match choice:
            case "1" | "text":
                mode = "text"
            case "2" | "voice":
                mode = "voice"
            case _:
                print("Invalid choice")
                return None
            
    
        result = run_auth(action, username, password, persona, mode)
    else:
        result = run_auth(action, username, password)

    if result is None:
        return None
    else:
        return {
            "username": result["username"],
            "user_id": result["user_id"],
            "persona": result["persona"],
            "mode": result["mode"]
        }

