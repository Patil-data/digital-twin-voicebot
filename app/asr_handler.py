import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

async def transcribe_audio(audio_bytes: bytes, filename: str = "audio.webm") -> str:
    if len(audio_bytes) < 1000:
        return ""
    transcription = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=(filename, audio_bytes, "audio/webm"),
    )
    print(f"[ASR] Transcribed: {transcription.text}")
    return transcription.text