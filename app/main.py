import sys, os
import threading
import time
from utils.loading import loading_animation

# suppress startup noise
sys.stderr = open(os.devnull, 'w')
sys.stdout = open(os.devnull, 'w')

from dotenv import load_dotenv
from routes.user import Auth
from routes.chat import start_chat

# restore
sys.stderr = sys.__stderr__
sys.stdout = sys.__stdout__

load_dotenv()

stop_event = threading.Event()
t = threading.Thread(target=loading_animation, args=(stop_event,))
t.start()

time.sleep(0.5)  #? small delay so animation is visible

stop_event.set()
t.join()

user = Auth()

if user is None:
    print("Exiting...")
else:
    print(f"Welcome back, {user['username']}!")
    start_chat(user)