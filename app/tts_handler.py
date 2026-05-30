import os
import io
from gtts import gTTS

def synthesize_speech(text: str) -> bytes:
    tts = gTTS(text=text, lang="en", slow=False)
    buffer = io.BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)
    return buffer.read()