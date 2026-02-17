import uuid
import bcrypt
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langgraph.graph import StateGraph,START, END
from typing import TypedDict, Optional

#* ------------------ Login / Sign-Up ------------------

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["ai-gf"]
users = db["users"]

#? Hash the Password
def hashing(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode, hashed)

class AuthState(TypedDict):
    action: str
    username: str
    password: str
    result: Optional[str]

def auth_node(state: AuthState):
    return state

#* Login
def login(state: AuthState):
    user = users.find_one({"username": state["username"]})

    if not user:
        print("user not found, signing up")
        state["result"] = "user_not_found"
        return state

    if verify_password(state["password"], user["password"]):
        state["result"] = "login_success"
    else:
        state["result"] = "wrong_password"

    return state

#* Signup
def signup(state: AuthState):
    if users.find_one({"username": state["username"]}):
        state["result"] = "user_already_exist"
        return state
    
    user_info = {
        "user_id": str(uuid.uuid4()),
        "username": state["username"],
        "password": hashing(state["password"])
    }

    users.insert_one(user_info)
    state["result"] = "signup_success"
    return state

def route_after_login(state: AuthState):
    if state["result"] == "user_not_found":
        return "signup"
    else: 
        return "end"

graph_builder = StateGraph(AuthState)

graph_builder.add_node("auth_node", auth_node)
graph_builder.add_node("login", login)
graph_builder.add_node("signup", signup)


graph_builder.add_edge(START, "auth_node")

graph_builder.add_conditional_edges(
    "auth_node",
    lambda state: state["action"],
    {
        "login": "login",
        "signup": "signup"
    }
)

graph_builder.add_conditional_edges(
    "login",
    route_after_login,
    {
        "signup": "signup",
        "end": END
    }
)
graph_builder.add_edge("signup", END)

graph = graph_builder.compile()

def run_auth(action: str, username: str, password: str):
    return graph.invoke({
        "action": action,
        "username": username,
        "password": password
    })