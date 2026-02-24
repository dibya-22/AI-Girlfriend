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
    
    result = run_auth(action, username, password)

    if result is None: return None
    else: return {"username": result["username"],"user_id": result["user_id"]}

