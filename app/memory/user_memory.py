import os
from dotenv import load_dotenv
from mem0 import Memory


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "BAAI/bge-large-en-v1.5"
        }
    },
    "llm": {
        "provider": "litellm",
        "config": {"api_key": GOOGLE_API_KEY, "model": "gemini/gemini-2.5-flash"}
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": os.getenv("NEO_CONNECTION_URI"),
            "username": os.getenv("NEO_USERNAME"),
            "password": os.getenv("NEO_PASSWORD")
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "embedding_model_dims": 1024,
            "collection_name": os.getenv("DB_NAME")
        }
    }
}

mem_client = Memory.from_config(config)

def add_memory(user_query: str, ai_response: str, user_id: str):
    mem_client.add(
        user_id=user_id,
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

def get_memory(user_query: str, user_id: str):
    return mem_client.search(query=user_query, user_id=user_id)
