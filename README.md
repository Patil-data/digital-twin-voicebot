---
title: Digital Twin Voicebot
emoji: 🎙️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 🎙️ Digital Twin Voicebot

A voice-to-voice AI that answers interview questions the way Shyamal Narayan Patil would. Speak a question in your browser and hear the answer out loud. No setup needed.

🔗 **Live demo:** [Try it here](https://huggingface.co/spaces/patilshyamalnarayan/digital-twin-voicebot)

Built for the Peerlist x Anthropic Voicebot Challenge.

---

## Demo

Click the orb, speak your question, and listen to the answer. You can also tap one of the preset questions.

---

## How It Works

```text
Microphone → Groq Whisper → Language model on Groq → Edge TTS → Audio answer
```

1. The browser records your voice.
2. Groq Whisper (`whisper-large-v3`) turns the audio into text.
3. A language model on Groq (`openai/gpt-oss-120b`) writes the answer using a written prompt about me.
4. Edge TTS turns the answer into speech and sends it back to the browser.

If the recording is empty or too short, the bot asks you to repeat the question.

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Backend | FastAPI (Python) |
| Speech to text | Groq Whisper (`whisper-large-v3`) |
| Language model | `openai/gpt-oss-120b` on Groq |
| Text to speech | Edge TTS (`en-US-JennyNeural`) |
| Frontend | HTML, CSS and vanilla JavaScript |
| Deployment | Hugging Face Spaces (Docker) |

---

## API Endpoints

| Endpoint | What it does |
|----------|--------------|
| `POST /ask` | Takes recorded audio and returns the spoken answer (MP3) |
| `POST /ask-text` | Takes a text question and returns the spoken answer (MP3) |
| `POST /ask-text-only` | Takes a text question and returns the answer as JSON text |

---

## Project Structure

```text
digital-twin-voicebot/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── twin.py          # Persona prompt and language model call
│   ├── asr_handler.py   # Speech to text with Groq Whisper
│   ├── tts_handler.py   # Text to speech with Edge TTS
│   └── static/
│       └── index.html   # Frontend
├── Dockerfile           # Container setup for Hugging Face Spaces
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment file
└── README.md
```

---

## Run Locally

```bash
git clone https://github.com/Patil-data/digital-twin-voicebot
cd digital-twin-voicebot
pip install -r requirements.txt
export GROQ_API_KEY=your_groq_api_key_here
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

On Windows, use `set GROQ_API_KEY=your_groq_api_key_here` instead of `export`.

Open `http://localhost:8000` in Chrome.

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Free key from [console.groq.com](https://console.groq.com) |

On Hugging Face, add it as a **secret** in the Space settings. Never put the key in the code.

---

## Good to Know

- The bot's knowledge comes from a written prompt about me in `app/twin.py`. It does not search documents.
- The audio is recorded first and then processed, so answers take a few seconds. It is not streaming word by word.
- An earlier version used Llama 3.3 70B on Groq. Groq retired that model, so I moved to a newer one.

---

## About

**Patil Shyamal Narayan**
B.Tech in Engineering Physics, IIT (ISM) Dhanbad, graduated 2026. Data Engineering Intern at Dynamite WebTech (2025). Math Trainer at Bhanzu.
I build backend and AI projects with Python and FastAPI.

GitHub: [Patil-data](https://github.com/Patil-data)
