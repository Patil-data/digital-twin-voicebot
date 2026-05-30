# 🎙️ Digital Twin Voicebot — Shyamal Narayan Patil

A voice-to-voice AI digital twin that answers interview questions exactly as I would — in real-time, from any browser, with zero setup required.

🔗 **Live Demo**: [huggingface.co/spaces/patilshyamalnarayan/digital-twin-voicebot](https://huggingface.co/spaces/patilshyamalnarayan/digital-twin-voicebot)

---

## What It Does
- 🎤 Click the orb to speak — ask me anything
- 🧠 AI understands your question and responds as me
- 🔊 Plays back the answer as audio in real-time
- 💬 Or click any of the 5 preset interview questions

---

## How It Works
```text
Browser mic → Groq Whisper (speech-to-text) → Llama 3.3 70B (answer as Shyamal) → gTTS (text-to-speech) → Audio playback

Tech StackLayerTechnologyBackendFastAPI (Python)Speech-to-TextGroq Whisper APILanguage ModelLlama 3.3 70B via GroqText-to-SpeechGoogle TTS (gTTS)FrontendVanilla HTML, CSS, JSDeploymentHugging Face Spaces (Docker)Project StructurePlaintextdigital-twin-voicebot/
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
Run LocallyBash# Clone the repo
git clone [https://github.com/Patil-data/digital-twin-voicebot](https://github.com/Patil-data/digital-twin-voicebot)
cd digital-twin-voicebot

# Install dependencies
pip install -r requirements.txt

# Set your Groq API key
export GROQ_API_KEY=your_groq_api_key_here

# Start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000
Then open http://localhost:8000 in Chrome.Environment VariablesVariableRequiredDescriptionGROQ_API_KEYYesFree API key from console.groq.comAbout MePatil Shyamal NarayanFinal-year Engineering Physics student at IIT (ISM) Dhanbad.Building at the intersection of AI systems, data engineering, and computational physics.Built for the Peerlist x Anthropic Voicebot Challenge
---

### Step 3: Push to GitHub
Once saved, run these three commands in your terminal one by one to push it directly to your GitHub repository:

```bash
git add README.md
git commit -m "add structured README"
git push origin main