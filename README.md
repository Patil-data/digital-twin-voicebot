---
title: Digital Twin Voicebot
emoji: 🎙️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 🎙️ Digital Twin Voicebot — Shyamal Narayan Patil

A voice-to-voice AI that answers interview questions exactly as I would — in real-time, from any browser, zero setup required.

🔗 **Live Demo** → [Try it here](https://huggingface.co/spaces/patilshyamalnarayan/digital-twin-voicebot)

---

## Demo

> Click the orb → speak your question → hear Shyamal answer in real-time

Supports both voice input and one-click preset questions.

---

## How It Works
Mic Input → Groq Whisper → Llama 3.3 70B → gTTS → Audio Response
1. Browser captures your voice
2. Groq Whisper transcribes it to text
3. Llama 3.3 70B generates a response in Shyamal's voice and persona
4. gTTS converts it to audio and plays it back

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Backend | FastAPI (Python) |
| Speech-to-Text | Groq Whisper API |
| Language Model | Llama 3.3 70B via Groq |
| Text-to-Speech | Google TTS (gTTS) |
| Frontend | HTML + CSS + Vanilla JS |
| Deployment | Hugging Face Spaces (Docker) |

---

## Project Structure

```text
digital-twin-voicebot/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── twin.py          # Persona, system prompt, LLM logic
│   ├── asr_handler.py   # Speech-to-text via Groq Whisper
│   ├── tts_handler.py   # Text-to-speech via gTTS
│   └── static/
│       └── index.html   # Frontend UI
├── Dockerfile           # Container config for HF Spaces
├── requirements.txt     # Python dependencies
└── README.md

---

## Run Locally

```bash
git clone https://github.com/Patil-data/digital-twin-voicebot
cd digital-twin-voicebot
pip install -r requirements.txt
export GROQ_API_KEY=your_groq_api_key_here
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000` in Chrome.

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Free key from [console.groq.com](https://console.groq.com) |

---

## About

**Patil Shyamal Narayan**
Final-year Engineering Physics student at IIT (ISM) Dhanbad.
Building at the intersection of AI systems, data engineering, and computational physics.

---

*Built for the Peerlist x Anthropic Voicebot Challenge*
