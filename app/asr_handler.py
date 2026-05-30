import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

async def transcribe_audio(audio_bytes: bytes, filename: str = "audio.webm") -> str:
    if len(audio_bytes) < 1000:
        print("[ASR] Audio too short, skipping")
        return ""
    print(f"[ASR] Received {len(audio_bytes)} bytes")
    transcription = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=("audio.wav", audio_bytes, "audio/webm"),
    )
    print(f"[ASR] Transcribed: {transcription.text}")
    return transcription.text