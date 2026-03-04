# AI GF - AI Girlfriend CLI

A command-line AI companion system built with modern backend architecture practices. Chat with an AI companion featuring user authentication, memory management, and voice capabilities.

## 🎯 Goal

Create a CLI AI system while practicing clean backend design principles and implementing a production-ready architecture.

## ✨ Features

- **User Authentication**: Secure registration and login with bcrypt password hashing
- **Persistent Memory**: User conversation history stored in MongoDB with Qdrant vector embeddings
- **Multiple Personas**: Support for different AI personas (Girlfriend, Boyfriend, Friend)
- **Voice Capabilities**: 
  - Speech-to-Text (STT) for voice input
  - Text-to-Speech (TTS) for voice output
- **LLM Integration**: Powered by Google's Gemini 2.5 Flash model via LangChain
- **Intelligent Chains**: LangGraph-based conversation chains with state management
- **Docker Support**: Easy deployment with Docker Compose

## 📁 Project Structure

```
ai_gf/
├── app/
│   ├── main.py                 # Entry point
│   ├── chains/                 # LLM chain logic
│   │   ├── __init__.py
│   │   └── chat.py            # Conversation graph and tools
│   ├── memory/                 # Memory management
│   │   ├── __init__.py
│   │   └── user_memory.py     # User conversation history
│   ├── prompts/                # AI persona definitions
│   │   ├── __init__.py
│   │   ├── default.py         # Default prompts
│   │   └── persona.py         # Persona templates
│   ├── routes/                 # Core functionality modules
│   │   ├── __init__.py
│   │   ├── auth.py            # User authentication flow
│   │   ├── chat.py            # Chat initiation
│   │   └── user.py            # User management
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   └── pass_input.py      # Input validation helpers
│   └── voice/                  # Voice processing
│       ├── __init__.py
│       ├── stt.py             # Speech-to-Text
│       └── tts.py             # Text-to-Speech
├── docker-compose.yml          # Container orchestration
├── requirement.txt             # Python dependencies
├── env.txt                     # Environment variables template
└── README.md
```

## 🛠️ Technologies Used

### Core Framework
- **FastAPI** - Web framework (setup in routes)
- **LangChain** - LLM framework
- **LangGraph** - Agentic workflows and state management
- **Google Gemini 2.5 Flash** - LLM model provider

### Databases
- **MongoDB** - User data and conversation storage
- **Qdrant** - Vector database for semantic search and memory retrieval

### Voice & Audio
- **Sarvam AI** - Text-to-Speech
- **SpeechRecognition** - Speech-to-Text

### Security & Utilities
- **bcrypt** - Password hashing
- **MongoDB Checkpointer** - LangGraph state persistence
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.8+
- MongoDB (can be run via Docker)
- Qdrant vector database (can be run via Docker)
- API Keys:
  - Google AI / Gemini API key
  - Sarvam API key (for voice)
  - MongoDB connection string

## 🚀 Installation

### 1. Clone and Setup

```bash
git clone https://github.com/dibya-22/AI-Girlfriend
cd ai_gf
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On Linux/Mac
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory (use `env.txt` as reference):

GOOGLE_API_KEY=

SARVAM_API_KEY=

MONGO_URI=
DB_NAME=

NEO_CONNECTION_URI=
NEO_USERNAME=
NEO_PASSWORD=
```

### 5. Start Databases (Docker)

```bash
docker-compose up -d
```

This starts:
- **MongoDB** on port 27017
- **Qdrant Vector DB** on port 6333

## 🎮 Running the Application

### Start the CLI

```bash
python app/main.py
```

### First Time Setup
1. Create a new account with username and password
2. Choose an AI persona (Girlfriend, Boyfriend, or Friend)
3. Start chatting!

### Existing Users
- Log in with your credentials
- Resume conversations with your AI companion
- Your conversation history is preserved

## 💬 Usage

### Text Chat
Simply type your message and press Enter. The AI will respond based on the selected persona.

### Voice Chat
1. Speak when prompted (STT will convert to text)
2. AI processes your message
3. Response is spoken back to you (TTS)

### Mode Switching
Use voice commands or text prompts to switch between text and voice modes.

## 🔐 Security Features

- **Bcrypt Hashing**: Passwords are hashed with bcrypt before storage
- **Session Management**: User sessions are managed securely
- **Input Validation**: All inputs are validated in `utils/pass_input.py`

## 📚 Architecture Highlights

### State Management
- Uses **LangGraph State** for managing conversation state
- MongoDB checkpointer for persistence across sessions

### Memory System
- Semantic memory using Qdrant embeddings
- User-specific conversation history
- Context-aware responses

### Agent Design
- Tool-based architecture for extensibility
- Mode switching capability (text/voice)
- Modular persona system

## 🔧 Configuration

### Adding New Personas

Edit `app/prompts/persona.py` to add new AI personas:

```python
YOUR_PERSONA = """
You are [describe your AI character here]
"""
```

### Customizing Voice Settings

Modify Sarvam AI settings in `app/voice/tts.py` for different voices and settings.

### Changing LLM Model

Update the model in `app/chains/chat.py`:

```python
llm = init_chat_model(
    model="your-model-name",
    model_provider="your-provider"
)
```

## 📊 Database Schema

### Users Collection
```json
{
  "_id": "ObjectId",
  "username": "string",
  "password": "bcrypt_hash",
  "created_at": "datetime",
  "persona": "girlfriend|boyfriend|friend"
}
```

### Conversations (via LangGraph Checkpoint)
- Stored in MongoDB with full message history
- Includes timestamps and user context

## 🐛 Troubleshooting

**Connection Issues to MongoDB/Qdrant**
- Ensure Docker containers are running: `docker-compose ps`
- Verify `.env` file has correct `MONGO_URI`

**API Key Errors**
- Check `.env` file is in root directory
- Verify API keys are correct and have required permissions

**Voice Not Working**
- Check ElevenLabs API key is valid
- Verify microphone permissions in system settings

## 🚀 Future Enhancements

- Web UI interface
- Multi-language support
- Advanced memory management (summarization, forgetting)
- Custom model fine-tuning
- Real-time streaming responses
- Social features (friend interactions)

## 📝 License

[Add your license here]

## 🤝 Contributing

Contributions are welcome! Please follow the existing code structure and clean backend design principles.

---

**Built with ❤️ using LangChain, LangGraph, and Google Gemini AI**
