import sys, os
from utils.color_print import forecolor
from utils.gettime import gettime

print("Loading...")

# suppress startup noise
sys.stderr = open(os.devnull, 'w')
sys.stdout = open(os.devnull, 'w')

from dotenv import load_dotenv
from routes.user import Auth
from routes.chat import start_chat

# restore
sys.stderr = sys.__stderr__
sys.stdout = sys.__stdout__

os.system("cls")

load_dotenv()

user = Auth()

if user is None:
    print(forecolor("Exiting...", "red"))
else:
    print(f"Good {gettime()}, {forecolor(user['username'], 'cyan')}!")
    start_chat(user)