import asyncio
import edge_tts
import io

async def synthesize_speech_async(text: str) -> bytes:
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-GuyNeural",
        rate="+5%",
        pitch="+0Hz"
    )
    buffer = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            buffer.write(chunk["data"])
    buffer.seek(0)
    return buffer.read()

def synthesize_speech(text: str) -> bytes:
    return asyncio.run(synthesize_speech_async(text))