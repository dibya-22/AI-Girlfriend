from routes.user import Auth
from routes.chat import start_chat

user = Auth()

if user is None:
    print("Exiting...")
else:
    print(f"Welcome back, {user['username']}!")
    start_chat(user)