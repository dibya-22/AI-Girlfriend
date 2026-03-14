# AI GF — CLI AI Companion

A command-line AI companion built with LangChain, LangGraph, and Google Gemini. Talk to an AI with persistent memory, multiple personas, and voice support.

> Built as a personal project to practice clean backend architecture while building something actually useful.

---

## What it does

- Login / Signup with secure password hashing
- Choose a persona — Girlfriend, Boyfriend, or Friend
- Chat via text or voice
- AI remembers things you tell it across sessions
- Switch between text and voice mid-conversation
- Indian accent (Sarvam AI) or American accent (ElevenLabs) TTS

---

## Tech Stack

| Category | Tools |
|---|---|
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain, LangGraph |
| Databases | MongoDB, Qdrant |
| Voice | Sarvam AI (TTS), ElevenLabs (TTS), SpeechRecognition (STT) |
| Auth | bcrypt |
| CLI | colorama, questionary |

---

## Project Structure

```
ai_gf/
├── app/
│   ├── main.py
│   ├── chains/
│   │   └── chat.py            # LangGraph conversation chain
│   ├── memory/
│   │   └── user_memory.py     # mem0 memory management
│   ├── prompts/
│   │   ├── default.py         # Base system prompt
│   │   └── persona.py         # Persona templates
│   ├── routes/
│   │   ├── auth.py            # Auth logic
│   │   ├── chat.py            # Chat loop
│   │   └── user.py            # User flow
│   ├── utils/
│   │   ├── color_print.py     # Terminal colors
│   │   ├── gettime.py         # Time of day helper
│   │   └── pass_input.py      # Masked password input
│   └── voice/
│       ├── stt.py             # Speech to Text
│       └── tts.py             # Text to Speech
├── docker-compose.yml
├── requirement.txt
└── .env
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/dibya-22/AI-Girlfriend
cd AI-Girlfriend
```

### 2. Create virtual environment

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Set up environment variables

Rename **`.env.example`** to **`.env`** and fill in your keys:
```env
GOOGLE_API_KEY=

# Voice API Keys
SARVAM_API_KEY=
ELEVENLABS_API_KEY=

MONGO_URI=
DB_NAME=

NEO_CONNECTION_URI=
NEO_USERNAME=
NEO_PASSWORD=
```

Or create a new `.env` file manually with the same keys._PASSWORD=
```

### 5. Start databases

```bash
docker-compose up -d
```

Starts MongoDB on port `27017` and Qdrant on port `6333`.

### 6. Run

```bash
python app/main.py
```

---

## First Time

1. Choose **Signup**
2. Enter username and password
3. Pick a persona — Girlfriend, Boyfriend, or Friend
4. Pick a mode — Text or Voice
5. Pick an accent — Indian or American
6. Start chatting

Returning users just log in and pick up where they left off.

---

## Voice Mode

- Speak when you see the `>` prompt
- Your speech is converted to text via Google Speech Recognition
- Response is spoken back using Sarvam AI or ElevenLabs based on your accent preference
- Say something like *"switch to text mode"* to switch mid-conversation

## Personas & Voices

Each persona has a dedicated voice based on accent preference:

| Persona | Indian Accent (Sarvam) | American Accent (ElevenLabs) |
|---|---|---|
| Girlfriend | Ishita | Bella |
| Boyfriend | Ratan | Will |
| Friend | Mani | Janet |

---

## Customization

### Add a new persona

Edit `app/prompts/persona.py`:

```python
YOUR_PERSONA = """
You are [describe your character here]
"""
```

Then add it to the `personas` dict in `app/chains/chat.py`.

### Change the LLM model

In `app/chains/chat.py`:

```python
llm = init_chat_model(
    model="your-model-name",
    model_provider="your-provider"
)
```

---

## Notes

- ElevenLabs free tier only supports default voices via API
- Make sure Docker is running before starting the app
- Microphone access is required for voice mode

---

**Built by [Dibya](https://github.com/dibya-22) <3**