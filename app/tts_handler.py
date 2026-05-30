import asyncio
import edge_tts
import io

async def _synthesize(text: str) -> bytes:
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural",
        rate="+5%"
    )
    buffer = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            buffer.write(chunk["data"])
    buffer.seek(0)
    return buffer.read()

def synthesize_speech(text: str) -> bytes:
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(asyncio.run, _synthesize(text))
                return future.result()
        return loop.run_until_complete(_synthesize(text))
    except Exception:
        asyncio.run(_synthesize(text))