import os
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.tools import tool
from prompts.default import SYSTEM
from prompts.persona import GIRL_FRIEND, BOY_FRIEND, FRIEND
from memory.user_memory import get_memory

load_dotenv()

llm = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai"
)


class State(TypedDict):
    messages: Annotated[list, add_messages]

@tool
def switch_mode(mode: str) -> str:
    """Switch between text and voice mode. Call when user requests a mode change."""
    return mode

@tool
def terminate() -> str:
    """Terminate the conversation when user wants to exit."""
    return "terminate"


llm_with_tools = llm.bind_tools([switch_mode, terminate])

def chatbot(state: State):
    response = llm_with_tools.invoke(state.get("messages"))
    return {"messages": [response]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

def get_graph():
    return MongoDBSaver.from_conn_string(
        os.getenv("MONGO_URI"),
        db_name=os.getenv("DB_NAME")
    )

def chat(user_query: str, user_id: str, persona: str , checkpointer)->str:
    graph = graph_builder.compile(checkpointer=checkpointer)
    config = {
        "configurable": {
            "thread_id": user_id
        }
    }

    personas = {
        "girlfriend": GIRL_FRIEND,
        "boyfriend": BOY_FRIEND,
        "friend": FRIEND
    }

    user_facts = get_memory(user_id, user_query)
    system = f"{SYSTEM}" + f"\n\n\nYour Persona:\n{personas[persona]}" + f"\n\n\nWhat you know about user:\n{user_facts}"

    final_state = graph.invoke(State({"messages": [SystemMessage(content=system), HumanMessage(content=user_query)]}), config)

    last_message = final_state['messages'][-1]

    if isinstance(last_message.content, list):
        content = " ".join([block["text"] for block in last_message.content if block.get("type") == "text"])
    else:
        content = last_message.content

    new_mode = None
    should_terminate = False

    for message in final_state["messages"]:
        if isinstance(message, AIMessage) and message.tool_calls:
            for tool_call in message.tool_calls:
                if tool_call["name"] == "switch_mode":
                    new_mode = tool_call["args"]["mode"]
                if tool_call["name"] == "terminate":
                    should_terminate = True
    
    return content, new_mode, should_terminate
